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
    if date_filter == 'all':
        start_date = None
    else:
        days = int(date_filter)
        start_date = timezone.now() - timedelta(days=days)
    
    # Sales Reports
    waste_orders = tbl_Order.objects.filter(tbl_orderitem__Item_Type='Waste').distinct()
    compost_orders = tbl_Order.objects.filter(tbl_orderitem__Item_Type='Compost').distinct()
    
    if start_date:
        waste_orders = waste_orders.filter(Order_Date__gte=start_date)
        compost_orders = compost_orders.filter(Order_Date__gte=start_date)
    
    # Revenue calculations
    waste_revenue = waste_orders.aggregate(total=Sum('Total_Amount'))['total'] or 0
    compost_revenue = compost_orders.aggregate(total=Sum('Total_Amount'))['total'] or 0
    total_revenue = waste_revenue + compost_revenue
    
    # Inventory Stats
    total_waste_stock = tbl_WasteInventory.objects.aggregate(total=Sum('available_quantity_kg'))['total'] or 0
    total_compost_stock = tbl_CompostBatch.objects.filter(Status='Available').aggregate(total=Sum('Stock_kg'))['total'] or 0
    
    # User Stats
    total_collectors = Collector.objects.filter(user__is_verified=True).count()
    total_compost_managers = CompostManager.objects.filter(user__is_verified=True).count()
    total_farmers = tbl_Order.objects.values('Buyer_id').distinct().count()
    
    # Payment Stats
    total_payments = tbl_PaymentTransaction.objects.filter(status='Success')
    if start_date:
        total_payments = total_payments.filter(transaction_date__gte=start_date)
    
    total_payment_amount = total_payments.aggregate(total=Sum('Amount'))['total'] or 0
    
    # Daily sales trend (last 7 days)
    seven_days_ago = timezone.now() - timedelta(days=7)
    daily_sales = tbl_Order.objects.filter(
        Order_Date__gte=seven_days_ago
    ).annotate(
        date=TruncDate('Order_Date')
    ).values('date').annotate(
        total=Sum('Total_Amount'),
        count=Count('Order_id')
    ).order_by('date')
    
    # Compost Manager Salaries (₹1000/day)
    daily_salary = 1000
    compost_managers = CompostManager.objects.filter(user__is_verified=True).select_related('user')
    
    # Calculate days worked (assuming they work every day they're verified)
    manager_salaries = []
    for manager in compost_managers:
        # Calculate days since joining
        join_date = manager.user.date_joined
        if start_date and join_date < start_date:
            days_worked = (timezone.now().date() - start_date.date()).days + 1
        else:
            days_worked = (timezone.now().date() - join_date.date()).days + 1
        
        total_salary = days_worked * daily_salary
        manager_salaries.append({
            'manager': manager,
            'days_worked': days_worked,
            'daily_rate': daily_salary,
            'total_salary': total_salary
        })
    
    total_salary_expense = sum(m['total_salary'] for m in manager_salaries)
    
    # Net profit (Revenue - Salary Expenses)
    net_profit = total_revenue - total_salary_expense
    
    context = {
        'period': date_filter,
        'waste_revenue': waste_revenue,
        'compost_revenue': compost_revenue,
        'total_revenue': total_revenue,
        'total_waste_stock': total_waste_stock,
        'total_compost_stock': total_compost_stock,
        'total_collectors': total_collectors,
        'total_compost_managers': total_compost_managers,
        'total_farmers': total_farmers,
        'total_payment_amount': total_payment_amount,
        'daily_sales': daily_sales,
        'manager_salaries': manager_salaries,
        'total_salary_expense': total_salary_expense,
        'net_profit': net_profit,
        'waste_orders_count': waste_orders.count(),
        'compost_orders_count': compost_orders.count(),
    }
    
    return render(request, 'Admin/reports.html', context)
