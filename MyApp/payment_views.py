from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.db.models import Sum, Count, Q
from django.utils import timezone
from MyApp.models import tbl_PaymentTransaction, tbl_Order
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
    
    # Calculate statistics
    total_transactions = transactions.count()
    total_amount = transactions.aggregate(total=Sum('Amount'))['total'] or 0
    
    success_count = transactions.filter(status='Success').count()
    pending_count = transactions.filter(status='Pending').count()
    failed_count = transactions.filter(status='Failed').count()
    
    success_amount = transactions.filter(status='Success').aggregate(total=Sum('Amount'))['total'] or 0
    
    # Payment method breakdown
    upi_count = transactions.filter(transaction_type='UPI').count()
    cod_count = transactions.filter(transaction_type='COD').count()
    
    upi_amount = transactions.filter(transaction_type='UPI', status='Success').aggregate(total=Sum('Amount'))['total'] or 0
    cod_amount = transactions.filter(transaction_type='COD', status='Success').aggregate(total=Sum('Amount'))['total'] or 0
    
    context = {
        'transactions': transactions[:100],  # Limit to 100 for performance
        'total_transactions': total_transactions,
        'total_amount': total_amount,
        'success_count': success_count,
        'pending_count': pending_count,
        'failed_count': failed_count,
        'success_amount': success_amount,
        'upi_count': upi_count,
        'cod_count': cod_count,
        'upi_amount': upi_amount,
        'cod_amount': cod_amount,
        'status_filter': status_filter,
        'type_filter': type_filter,
        'period_filter': period_filter,
    }
    
    return render(request, 'Admin/payment_transactions.html', context)
