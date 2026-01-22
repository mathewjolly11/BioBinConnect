from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.db.models import Sum, Count, Avg
from django.db.models.functions import TruncDate, TruncMonth
from django.utils import timezone
from MyApp.models import (
    tbl_Order, tbl_OrderItem, tbl_PaymentTransaction, 
    tbl_WasteInventory, tbl_CompostBatch, tbl_FarmerSupply
)
from GuestApp.models import Collector, CompostManager
from datetime import datetime, timedelta
from decimal import Decimal


@login_required(login_url='login')
@never_cache
def admin_reports(request):
    """Comprehensive admin reports dashboard"""
    
    # Date filters
    date_filter = request.GET.get('period', '30')  # Default 30 days
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')
    
    start_date = None
    end_date = None
    
    if date_filter == 'custom' and start_date_str and end_date_str:
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            # For end date, we want to include the entire day, so we set it to the next day's midnight if comparing with datetime
            # or just use the date if comparing with date objects. 
            # Given models likely use DateTimeField (auto_now_add=True), user inputs '2023-01-01', we want up to '2023-01-01 23:59:59'
            # Simplest is: start >= start_date AND start < end_date + 1 day
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d') + timedelta(days=1) 
        except ValueError:
            pass
    elif date_filter == 'all':
        start_date = None
    else:
        try:
            days = int(date_filter)
            start_date = timezone.now() - timedelta(days=days)
        except (ValueError, TypeError):
            # Fallback to 30 days if invalid
            start_date = timezone.now() - timedelta(days=30)
    
    # Sales Reports
    waste_orders = tbl_Order.objects.filter(tbl_orderitem__Item_Type='Waste').distinct()
    compost_orders = tbl_Order.objects.filter(tbl_orderitem__Item_Type='Compost').distinct()
    
    if start_date:
        waste_orders = waste_orders.filter(Order_Date__gte=start_date)
        compost_orders = compost_orders.filter(Order_Date__gte=start_date)
        
    if end_date:
        waste_orders = waste_orders.filter(Order_Date__lt=end_date)
        compost_orders = compost_orders.filter(Order_Date__lt=end_date)
    
    # Revenue calculations
    waste_revenue = waste_orders.aggregate(total=Sum('Total_Amount'))['total'] or 0
    compost_revenue = compost_orders.aggregate(total=Sum('Total_Amount'))['total'] or 0
    total_revenue = waste_revenue + compost_revenue
    
    # Inventory Stats
    total_waste_stock = tbl_WasteInventory.objects.filter(
        status='Available'
    ).aggregate(total=Sum('available_quantity_kg'))['total'] or 0
    total_compost_stock = tbl_CompostBatch.objects.filter(Status='Ready').aggregate(total=Sum('Stock_kg'))['total'] or 0
    
    # User Stats (Active/Approved Users)
    from GuestApp.models import CustomUser
    total_households = CustomUser.objects.filter(role='household', account_status='Approved').count()
    total_farmers_count = CustomUser.objects.filter(role='farmer', account_status='Approved').count()
    total_collectors_count = CustomUser.objects.filter(role='collector', account_status='Approved').count()
    total_compost_managers_count = CustomUser.objects.filter(role='compost_manager', account_status='Approved').count()
    
    # Aliasing for compatibility with existing export/template logic
    total_collectors = total_collectors_count
    total_farmers = total_farmers_count
    total_compost_managers = total_compost_managers_count

    # Existing counts used mainly for "Orders" logic, can keep or replace. 
    # The template uses 'total_collectors' and 'total_compost_managers' but defined via models. 
    # Let's keep existing logic for template compatibility but add new variables for charts.
    chart_user_data = {
        'households': total_households,
        'farmers': total_farmers_count,
        'collectors': total_collectors_count
    }

    # Revenue Breakdown
    # Waste & Compost Revenue calculated above
    
    # Household Fees Revenue
    # Checking both potential types to be safe based on legacy vs model definition
    fees_revenue = tbl_PaymentTransaction.objects.filter(
        status='Success',
        transaction_type__in=['HouseholdDaily', 'HouseholdPayment']
    ).aggregate(total=Sum('Amount'))['total'] or 0
    
    # If date filters are applied, filter fees too
    fees_query = tbl_PaymentTransaction.objects.filter(
        status='Success', 
        transaction_type__in=['HouseholdDaily', 'HouseholdPayment']
    )
    if start_date:
        fees_query = fees_query.filter(transaction_date__gte=start_date)
    if end_date:
         fees_query = fees_query.filter(transaction_date__lt=end_date)
    fees_revenue = fees_query.aggregate(total=Sum('Amount'))['total'] or 0

    # Total Revenue should theoretically include Fees, but current dashboard shows Waste+Compost.
    # We will keep 'total_revenue' as is for consistency with existing cards, 
    # OR update it. Let's keep it as is to avoid confusion, but show Fees in chart.
    
    # 6-Month Trend Analysis
    six_months_ago = timezone.now() - timedelta(days=180)
    
    # Monthly Revenue (Waste + Compost orders)
    monthly_revenue_data = tbl_Order.objects.filter(
        Order_Date__gte=six_months_ago,
        Payment_Status='Paid'
    ).annotate(
        month=TruncMonth('Order_Date')
    ).values('month').annotate(
        total=Sum('Total_Amount')
    ).order_by('month')
    
    # Monthly Expenses (Salaries)
    monthly_expense_data = tbl_PaymentTransaction.objects.filter(
        transaction_date__gte=six_months_ago,
        status='Success',
        transaction_type__in=['CollectorSalary', 'ManagerSalary']
    ).annotate(
        month=TruncMonth('transaction_date')
    ).values('month').annotate(
        total=Sum('Amount')
    ).order_by('month')
    
    # Merge into a list of months
    trend_labels = []
    trend_revenue = []
    trend_expense = []
    
    # Create a dict for easy lookup
    rev_dict = {item['month'].strftime('%Y-%m'): item['total'] for item in monthly_revenue_data if item['month']}
    exp_dict = {item['month'].strftime('%Y-%m'): item['total'] for item in monthly_expense_data if item['month']}
    
    # Generate last 6 months list
    current_date = timezone.now().date()
    for i in range(5, -1, -1):
        d = current_date - timedelta(days=i*30) # Approx
        month_key = d.strftime('%Y-%m')
        month_label = d.strftime('%b %Y')
        trend_labels.append(month_label)
        trend_revenue.append(float(rev_dict.get(month_key, 0)))
        trend_expense.append(float(exp_dict.get(month_key, 0)))

    # --- ADDITIONAL STATISTICS ---

    # 1. Daily sales trend (last 7 days)
    seven_days_ago = timezone.now() - timedelta(days=7)
    daily_sales = tbl_Order.objects.filter(
        Order_Date__gte=seven_days_ago
    ).annotate(
        date=TruncDate('Order_Date')
    ).values('date').annotate(
        total=Sum('Total_Amount'),
        count=Count('Order_id')
    ).order_by('date')

    # 2. Payment Stats (Total received payments)
    total_payments = tbl_PaymentTransaction.objects.filter(status='Success')
    if start_date:
        total_payments = total_payments.filter(transaction_date__gte=start_date)
    if end_date:
        total_payments = total_payments.filter(transaction_date__lt=end_date)
    
    total_payment_amount = total_payments.aggregate(total=Sum('Amount'))['total'] or 0

    # 3. Salary Expenses for the selected period
    salary_payments = tbl_PaymentTransaction.objects.filter(
        status='Success',
        transaction_type__in=['CollectorSalary', 'ManagerSalary']
    )
    if start_date:
        salary_payments = salary_payments.filter(transaction_date__gte=start_date)
    if end_date:
        salary_payments = salary_payments.filter(transaction_date__lt=end_date)
    
    # Total salary expense and breakdown
    total_salary_expense = salary_payments.aggregate(total=Sum('Amount'))['total'] or 0
    collector_salary_expense = salary_payments.filter(transaction_type='CollectorSalary').aggregate(total=Sum('Amount'))['total'] or 0
    manager_salary_expense = salary_payments.filter(transaction_type='ManagerSalary').aggregate(total=Sum('Amount'))['total'] or 0
    
    # 4. Net Profit
    net_profit = total_revenue - total_salary_expense
    
    # --- END STATISTICS ---

    # Handle Export
    export_type = request.GET.get('export')
    if export_type:
        from MyApp.utils import generate_pdf_report, generate_excel_report
        from django.http import HttpResponse
        
        content_type = 'application/pdf' if export_type == 'pdf' else 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        extension = 'pdf' if export_type == 'pdf' else 'xlsx'
        response = HttpResponse(content_type=content_type)
        filename_date = f"{start_date_str}_to_{end_date_str}" if date_filter == 'custom' and start_date_str else timezone.now().strftime("%Y-%m-%d")
        response['Content-Disposition'] = f'attachment; filename="Admin_Report_{filename_date}.{extension}"'
        
        range_label = f"{start_date_str} to {end_date_str}" if date_filter == 'custom' else ('All Time' if date_filter=='all' else f'Last {date_filter} Days')
        title = f"Admin Report ({range_label})"
        headers = ["Metric", "Value"]
        data = [
            ["Total Revenue", f"Rs. {total_revenue:.2f}"],
            ["Salary Expenses", f"Rs. {total_salary_expense:.2f}"],
            ["Net Profit", f"Rs. {net_profit:.2f}"],
            ["Waste Sales Revenue", f"Rs. {waste_revenue:.2f}"],
            ["Compost Sales Revenue", f"Rs. {compost_revenue:.2f}"],
            ["Total Payments Received", f"Rs. {total_payment_amount:.2f}"],
            ["Current Waste Stock", f"{total_waste_stock:.2f} kg"],
            ["Current Compost Stock", f"{int(total_compost_stock)} packets"],
            ["Active Collectors", str(total_collectors)],
            ["Active Compost Managers", str(total_compost_managers)],
            ["Active Farmers", str(total_farmers)],
        ]
        
        if export_type == 'pdf':
            generate_pdf_report(response, title, headers, data)
        elif export_type == 'excel':
            generate_excel_report(response, title, headers, data)
            
        return response

    context = {
        'total_orders': waste_orders.count() + compost_orders.count(), # Approx
        'total_revenue': total_revenue,
        'waste_revenue': waste_revenue,
        'compost_revenue': compost_revenue,
        'fees_revenue': fees_revenue,
        
        'total_waste_stock': total_waste_stock,
        'total_compost_stock': total_compost_stock,
        
        'total_collectors': total_collectors,
        'total_compost_managers': total_compost_managers,
        
        'total_salary_expense': total_salary_expense,
        'collector_salary_expense': collector_salary_expense,
        'manager_salary_expense': manager_salary_expense,
        'net_profit': net_profit,
        
        'waste_orders_count': waste_orders.count(),
        'compost_orders_count': compost_orders.count(),
        
        'total_payment_amount': total_payment_amount,
        
        'manager_salaries': [], # Placeholder if you don't have the object list logic here, or passed from elsewhere
        
        'period': date_filter,
        'custom_start_date': start_date_str if start_date_str else '',
        'custom_end_date': end_date_str if end_date_str else '',
        
        # Chart Data
        'chart_revenue_split': [float(waste_revenue), float(compost_revenue), float(fees_revenue)],
        'chart_user_data': [total_households, total_farmers_count, total_collectors_count],
        'trend_labels': trend_labels,
        'trend_revenue': trend_revenue,
        'trend_expense': trend_expense,
    }
    
    return render(request, 'Admin/reports.html', context)
