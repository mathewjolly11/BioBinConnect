from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.db.models import Sum, Count, Q
from django.utils import timezone
from MyApp.models import tbl_PaymentTransaction, tbl_Order, tbl_OrderItem, tbl_HouseholdPayment
from GuestApp.models import CompostManager
from datetime import timedelta


@login_required(login_url='login')
@never_cache
def payment_transactions(request):
    """Comprehensive payment transactions report"""
    
    # Get filter parameters
    status_filter = request.GET.get('status', 'all')
    type_filter = request.GET.get('type', 'all')
    period_filter = request.GET.get('period', '30')
    
    # Base queryset
    transactions = tbl_PaymentTransaction.objects.all().select_related('Payer_id', 'Receiver_id')
    
    # Apply filters
    if status_filter != 'all':
        transactions = transactions.filter(status=status_filter)
    
    if type_filter != 'all':
        transactions = transactions.filter(transaction_type=type_filter)
    
    # Date filter
    if period_filter != 'all':
        days = int(period_filter)
        start_date = timezone.now() - timedelta(days=days)
        transactions = transactions.filter(transaction_date__gte=start_date)
    
    # Order by latest first
    transactions = transactions.order_by('-transaction_date')
    
    # Handle Export
    if request.GET.get('export') == 'excel':
        from MyApp.utils import generate_excel_report
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="Payment_Transactions_{timezone.now().strftime("%Y-%m-%d")}.xlsx"'
        
        headers = ["Txn ID", "Date", "Payer", "Receiver", "Amount", "Type", "Status", "Reference"]
        data = []
        
        for txn in transactions:
            data.append([
                txn.Transaction_id,
                txn.transaction_date.strftime('%Y-%m-%d %H:%M'),
                txn.Payer_id.name,
                txn.Receiver_id.name,
                txn.Amount,
                txn.transaction_type,
                txn.status,
                txn.Reference_id or "-"
            ])
            
        generate_excel_report(response, "Payment Transactions Report", headers, data)
        return response
    
    # Calculate statistics
    total_transactions = transactions.count()
    total_amount = transactions.aggregate(total=Sum('Amount'))['total'] or 0
    
    success_count = transactions.filter(status='Success').count()
    pending_count = transactions.filter(status='Pending').count()
    failed_count = transactions.filter(status='Failed').count()
    
    success_amount = transactions.filter(status='Success').aggregate(total=Sum('Amount'))['total'] or 0
    
    # Payment type breakdown (actual transaction types)
    household_count = transactions.filter(transaction_type='HouseholdDaily').count()
    compost_count = transactions.filter(transaction_type='CompostSale').count()
    waste_count = transactions.filter(transaction_type='WasteSale').count()
    salary_count = transactions.filter(transaction_type='CollectorSalary').count()
    
    household_amount = transactions.filter(transaction_type='HouseholdDaily', status='Success').aggregate(total=Sum('Amount'))['total'] or 0
    compost_amount = transactions.filter(transaction_type='CompostSale', status='Success').aggregate(total=Sum('Amount'))['total'] or 0
    waste_amount = transactions.filter(transaction_type='WasteSale', status='Success').aggregate(total=Sum('Amount'))['total'] or 0
    salary_amount = transactions.filter(transaction_type='CollectorSalary', status='Success').aggregate(total=Sum('Amount'))['total'] or 0
    
    context = {
        'transactions': transactions,  # Show all transactions (removed limit)
        'total_transactions': total_transactions,
        'total_amount': total_amount,
        'success_count': success_count,
        'pending_count': pending_count,
        'failed_count': failed_count,
        'success_amount': success_amount,
        # Actual transaction types
        'household_count': household_count,
        'compost_count': compost_count,
        'waste_count': waste_count,
        'salary_count': salary_count,
        'household_amount': household_amount,
        'compost_amount': compost_amount,
        'waste_amount': waste_amount,
        'salary_amount': salary_amount,
        'status_filter': status_filter,
        'type_filter': type_filter,
        'period_filter': period_filter,
    }
    
    return render(request, 'Admin/payment_transactions.html', context)


@login_required(login_url='login')
@never_cache
def payment_revenue_analytics(request):
    """Comprehensive payment revenue analytics dashboard with profit calculation"""
    from GuestApp.models import Collector, CompostManager, Farmer, Household
    from MyApp.models import tbl_HouseholdPayment, tbl_OrderItem
    
    # Get filter parameters
    period_filter = request.GET.get('period', '30')
    
    # Base querysets
    orders = tbl_Order.objects.filter(Payment_Status='Paid')
    order_items = tbl_OrderItem.objects.select_related('Order_id').filter(Order_id__Payment_Status='Paid')
    household_payments = tbl_HouseholdPayment.objects.filter(status='Completed')
    
    # Date filter
    if period_filter != 'all':
        days = int(period_filter)
        start_date = timezone.now() - timedelta(days=days)
        orders = orders.filter(Order_Date__gte=start_date)
        order_items = order_items.filter(Order_id__Order_Date__gte=start_date)
        household_payments = household_payments.filter(payment_date__gte=start_date)
    
    # REVENUE CALCULATIONS
    # 1. Waste Order Revenue
    waste_order_items = order_items.filter(Item_Type='Waste')
    waste_order_revenue = 0
    waste_order_count = 0
    for item in waste_order_items:
        waste_order_revenue += item.Quantity_kg * item.Unit_Price
        waste_order_count += 1
    
    # 2. Compost Order Revenue  
    compost_order_items = order_items.filter(Item_Type='Compost')
    compost_order_revenue = 0
    compost_order_count = 0
    for item in compost_order_items:
        compost_order_revenue += item.Quantity_kg * item.Unit_Price
        compost_order_count += 1
    
    # 3. Household Payment Revenue
    total_household_revenue = household_payments.aggregate(total=Sum('amount'))['total'] or 0
    total_household_count = household_payments.count()
    
    # Total Revenue
    total_revenue = waste_order_revenue + compost_order_revenue + total_household_revenue
    
    # EXPENSE CALCULATIONS
    # Salary Expenses - Equal pay for managers and collectors
    daily_manager_salary = 1000   # Manager daily salary  
    daily_collector_salary = 1000  # Collector daily salary (same as managers)
    
    # Manager salaries calculation
    managers = CompostManager.objects.filter(user__is_verified=True)
    total_manager_salary = 0
    
    if period_filter != 'all':
        # Calculate based on actual working days for each manager
        period_start_date = start_date.date()
        period_end_date = timezone.now().date()
        
        for manager in managers:
            # Get manager's join date
            manager_join_date = manager.user.date_joined.date() if hasattr(manager.user, 'date_joined') else period_start_date
            
            # Calculate actual working period for this manager
            manager_work_start = max(manager_join_date, period_start_date)
            manager_work_end = period_end_date
            
            # Only calculate if manager actually worked during this period
            if manager_work_end >= manager_work_start:
                days_worked = (manager_work_end - manager_work_start).days + 1
                total_manager_salary += days_worked * daily_manager_salary
    else:
        # All time calculation - calculate from each manager's join date to now
        current_date = timezone.now().date()
        for manager in managers:
            manager_join_date = manager.user.date_joined.date() if hasattr(manager.user, 'date_joined') else current_date
            days_worked = (current_date - manager_join_date).days + 1
            total_manager_salary += max(days_worked, 0) * daily_manager_salary
    
    # Collector salaries - calculate based on actual working days like managers
    collector_salary_expense = 0
    try:
        # First try to get from payment transactions
        transactions = tbl_PaymentTransaction.objects.filter(status='Success', transaction_type='CollectorSalary')
        if period_filter != 'all':
            transactions = transactions.filter(transaction_date__gte=start_date)
        collector_salary_expense = transactions.aggregate(total=Sum('Amount'))['total'] or 0
        
        # If no payment transactions found, calculate based on actual working days
        if collector_salary_expense == 0:
            from GuestApp.models import Collector
            collectors = Collector.objects.filter(is_active=True)
            
            if period_filter != 'all':
                # Calculate based on actual working days for each collector in the period
                period_start_date = start_date.date()
                period_end_date = timezone.now().date()
                
                for collector in collectors:
                    # Get collector's join date
                    collector_join_date = collector.user.date_joined.date() if hasattr(collector.user, 'date_joined') else period_start_date
                    
                    # Calculate actual working period for this collector
                    collector_work_start = max(collector_join_date, period_start_date)
                    collector_work_end = period_end_date
                    
                    # Only calculate if collector actually worked during this period
                    if collector_work_end >= collector_work_start:
                        days_worked = (collector_work_end - collector_work_start).days + 1
                        collector_salary_expense += days_worked * daily_collector_salary
            else:
                # All time calculation - calculate from each collector's join date to now
                current_date = timezone.now().date()
                for collector in collectors:
                    collector_join_date = collector.user.date_joined.date() if hasattr(collector.user, 'date_joined') else current_date
                    days_worked = (current_date - collector_join_date).days + 1
                    collector_salary_expense += max(days_worked, 0) * daily_collector_salary
    except Exception as e:
        collector_salary_expense = 0
    
    # Total Expenses
    total_expenses = total_manager_salary + collector_salary_expense
    
    # PROFIT CALCULATION
    gross_profit = total_revenue - total_expenses
    profit_margin = (gross_profit / total_revenue * 100) if total_revenue > 0 else 0
    
    # Daily revenue/profit for charts (last 7 days)
    daily_data = []
    for i in range(6, -1, -1):
        date = timezone.now().date() - timedelta(days=i)
        
        # Daily waste order revenue
        day_waste_items = waste_order_items.filter(Order_id__Order_Date__date=date)
        day_waste_revenue = sum(item.Quantity_kg * item.Unit_Price for item in day_waste_items)
        
        # Daily compost order revenue
        day_compost_items = compost_order_items.filter(Order_id__Order_Date__date=date)
        day_compost_revenue = sum(item.Quantity_kg * item.Unit_Price for item in day_compost_items)
        
        # Daily household payments
        day_household = household_payments.filter(payment_date__date=date).aggregate(total=Sum('amount'))['total'] or 0
        
        day_revenue = day_waste_revenue + day_compost_revenue + day_household
        
        # Daily expenses (manager salaries for that day)
        day_manager_expense = managers.count() * daily_manager_salary
        try:
            day_collector_expense = tbl_PaymentTransaction.objects.filter(
                transaction_date__date=date, 
                transaction_type='CollectorSalary',
                status='Success'
            ).aggregate(total=Sum('Amount'))['total'] or 0
            
            # If no payment transaction for collectors, use estimated daily salary
            if day_collector_expense == 0:
                try:
                    from GuestApp.models import Collector
                    collectors = Collector.objects.filter(is_active=True)
                    day_collector_expense = collectors.count() * daily_collector_salary
                except:
                    day_collector_expense = 0
        except:
            day_collector_expense = 0
        
        day_expenses = day_manager_expense + day_collector_expense
        day_profit = day_revenue - day_expenses
        
        daily_data.append({
            'date': date.strftime('%m/%d'),
            'revenue': day_revenue,
            'expenses': day_expenses,
            'profit': day_profit
        })
    
    # Top payment receivers (from payment transactions if exists)
    top_receivers = []
    try:
        transactions_all = tbl_PaymentTransaction.objects.filter(status='Success')
        if period_filter != 'all':
            transactions_all = transactions_all.filter(transaction_date__gte=start_date)
        top_receivers = transactions_all.values('Receiver_id__name').annotate(
            total_received=Sum('Amount'),
            transaction_count=Count('Transaction_id')
        ).order_by('-total_received')[:5]
    except:
        top_receivers = []
    
    # Recent high-value transactions
    recent_transactions = []
    try:
        recent_transactions = tbl_PaymentTransaction.objects.filter(status='Success').order_by('-Amount')[:10]
    except:
        recent_transactions = []
    
    context = {
        # Revenue breakdown
        'waste_order_revenue': waste_order_revenue,
        'compost_order_revenue': compost_order_revenue, 
        'household_revenue': total_household_revenue,
        'total_revenue': total_revenue,
        
        # Expense breakdown
        'total_manager_salary': total_manager_salary,
        'collector_salary_expense': collector_salary_expense,
        'total_expenses': total_expenses,
        
        # Profit metrics
        'gross_profit': gross_profit,
        'profit_margin': profit_margin,
        
        # Count metrics
        'waste_order_count': waste_order_count,
        'compost_order_count': compost_order_count,
        'household_count': total_household_count,
        'total_transactions': waste_order_count + compost_order_count + total_household_count,
        
        # Chart data
        'daily_data': daily_data,
        
        # Top lists
        'top_receivers': top_receivers,
        'recent_transactions': recent_transactions,
        
        # Period info
        'period_filter': period_filter,
        'start_date': start_date.strftime('%Y-%m-%d') if start_date else None,
    }
    
    return render(request, 'Admin/payment_revenue_analytics.html', context)


@login_required(login_url='login')
@never_cache
def collector_salaries(request):
    """Collector Salaries - Shows actual payments made via Salary Management"""
    
    # Get filter parameters
    period_filter = request.GET.get('period', '30')
    
    # Date filtering
    start_date = None
    if period_filter != 'all':
        days = int(period_filter)
        start_date = timezone.now() - timedelta(days=days)
    
    # Get actual salary payments from transactions
    salary_payments = tbl_PaymentTransaction.objects.filter(
        status='Success',
        transaction_type='CollectorSalary'
    ).select_related('Receiver_id')
    
    if start_date:
        salary_payments = salary_payments.filter(transaction_date__gte=start_date)
    
    # Group payments by collector
    from django.db.models import Sum, Count
    collector_payment_summary = salary_payments.values(
        'Receiver_id',
        'Receiver_id__name',
        'Receiver_id__email'
    ).annotate(
        total_paid=Sum('Amount'),
        payment_count=Count('Transaction_id')
    ).order_by('-total_paid')
    
    # Get all collectors for complete view
    try:
        from GuestApp.models import Collector
        all_collectors = Collector.objects.filter(is_active=True).select_related('user')
    except:
        all_collectors = []
    
    # Build collector data with payment info
    collector_salaries_data = []
    total_salary_paid = 0
    
    for collector in all_collectors:
        # Find payment summary for this collector
        paid_amount = 0
        payment_count = 0
        
        for summary in collector_payment_summary:
            if summary['Receiver_id'] == collector.user.id:
                paid_amount = summary['total_paid'] or 0
                payment_count = summary['payment_count'] or 0
                break
        
        total_salary_paid += paid_amount
        
        collector_salaries_data.append({
            'collector': collector,
            'name': collector.collector_name if hasattr(collector, 'collector_name') else collector.user.username,
            'email': collector.user.email if hasattr(collector.user, 'email') else 'N/A',
            'phone': collector.phone if hasattr(collector, 'phone') else 'N/A',
            'total_paid': paid_amount,
            'payment_count': payment_count,
            'has_payments': paid_amount > 0
        })
    
    # Sort by total paid (descending)
    collector_salaries_data.sort(key=lambda x: x['total_paid'], reverse=True)
    
    context = {
        'collector_salaries': collector_salaries_data,
        'total_salary_paid': total_salary_paid,
        'total_collectors': len(collector_salaries_data),
        'collectors_with_payments': sum(1 for c in collector_salaries_data if c['has_payments']),
        'daily_rate': 1000,  # Reference rate
        'period_filter': period_filter,
        'start_date': start_date.strftime('%Y-%m-%d') if start_date else None,
    }
    
    return render(request, 'Admin/collector_salaries.html', context)
