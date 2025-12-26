from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from MyApp.models import tbl_Order, tbl_OrderItem, tbl_FarmerSupply, tbl_PaymentTransaction
from django.db.models import Sum, Count, Q
from decimal import Decimal


@login_required(login_url='login')
@never_cache
def admin_waste_sales(request):
    """Admin view for waste sales tracking"""
    
    # Get all waste orders
    waste_orders = tbl_Order.objects.filter(
        orderitem__Item_Type='Waste'
    ).distinct().select_related('Buyer_id').prefetch_related('orderitem_set').order_by('-Date_Ordered')
    
    # Apply filters
    status_filter = request.GET.get('status', 'all')
    if status_filter != 'all':
        waste_orders = waste_orders.filter(Payment_Status=status_filter)
    
    # Calculate statistics
    total_orders = waste_orders.count()
    total_revenue = waste_orders.aggregate(total=Sum('Total_Amount'))['total'] or Decimal('0.00')
    pending_orders = waste_orders.filter(Payment_Status='Pending').count()
    completed_orders = waste_orders.filter(Payment_Status='Paid').count()
    
    context = {
        'orders': waste_orders,
        'status_filter': status_filter,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'pending_orders': pending_orders,
        'completed_orders': completed_orders,
    }
    return render(request, 'Admin/waste_sales.html', context)


@login_required(login_url='login')
@never_cache
def admin_compost_sales(request):
    """Admin view for compost sales tracking"""
    
    # Get all compost orders
    compost_orders = tbl_Order.objects.filter(
        orderitem__Item_Type='Compost'
    ).distinct().select_related('Buyer_id').prefetch_related('orderitem_set').order_by('-Date_Ordered')
    
    # Apply filters
    status_filter = request.GET.get('status', 'all')
    if status_filter != 'all':
        compost_orders = compost_orders.filter(Payment_Status=status_filter)
    
    # Calculate statistics
    total_orders = compost_orders.count()
    total_revenue = compost_orders.aggregate(total=Sum('Total_Amount'))['total'] or Decimal('0.00')
    pending_orders = compost_orders.filter(Payment_Status='Pending').count()
    completed_orders = compost_orders.filter(Payment_Status='Paid').count()
    
    context = {
        'orders': compost_orders,
        'status_filter': status_filter,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'pending_orders': pending_orders,
        'completed_orders': completed_orders,
    }
    return render(request, 'Admin/compost_sales.html', context)


@login_required(login_url='login')
@never_cache
def admin_update_delivery_status(request, order_id):
    """Update delivery status for an order"""
    if request.method == 'POST':
        try:
            order = tbl_Order.objects.get(Order_id=order_id)
            new_status = request.POST.get('delivery_status')
            
            # Update all order items
            order.orderitem_set.all().update(Delivery_Status=new_status)
            
            messages.success(request, f'Delivery status updated to {new_status}')
        except Exception as e:
            messages.error(request, f'Error updating status: {str(e)}')
    
    # Redirect back to appropriate page
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)
