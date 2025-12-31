from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from MyApp.models import tbl_Order, tbl_OrderItem, tbl_FarmerSupply, tbl_PaymentTransaction, tbl_WasteInventory
from GuestApp.models import Collector
from django.db.models import Sum, Count, Q
from decimal import Decimal


@login_required(login_url='login')
@never_cache
def admin_waste_sales(request):
    """Admin view for waste sales tracking"""
    
    # Get all waste orders
    waste_orders = tbl_Order.objects.filter(
        tbl_orderitem__Item_Type='Waste'
    ).distinct().select_related('Buyer_id', 'assigned_collector').prefetch_related('tbl_orderitem_set').order_by('-Order_Date')
    
    # Apply filters
    status_filter = request.GET.get('status', 'all')
    if status_filter != 'all':
        waste_orders = waste_orders.filter(Payment_Status=status_filter)
    
    # Calculate statistics
    total_orders = waste_orders.count()
    total_revenue = waste_orders.aggregate(total=Sum('Total_Amount'))['total'] or Decimal('0.00')
    pending_orders = waste_orders.filter(Payment_Status='Pending').count()
    completed_orders = waste_orders.filter(Payment_Status='Paid').count()
    
    # Add total_quantity to each order
    waste_orders_list = list(waste_orders)
    for order in waste_orders_list:
        total_qty = Decimal('0.00')
        for item in order.tbl_orderitem_set.all():
            total_qty += item.Quantity_kg
        order.total_quantity = total_qty
    
    # Get all collectors for assignment dropdown
    collectors = Collector.objects.filter(user__is_active=True)
    
    context = {
        'orders': waste_orders_list,
        'collectors': collectors,
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
        tbl_orderitem__Item_Type='Compost'
    ).distinct().select_related('Buyer_id').prefetch_related('tbl_orderitem_set').order_by('-Order_Date')
    
    # Apply filters
    status_filter = request.GET.get('status', 'all')
    if status_filter != 'all':
        compost_orders = compost_orders.filter(Payment_Status=status_filter)
    
    # Calculate statistics
    total_orders = compost_orders.count()
    total_revenue = compost_orders.aggregate(total=Sum('Total_Amount'))['total'] or Decimal('0.00')
    pending_orders = compost_orders.filter(Payment_Status='Pending').count()
    completed_orders = compost_orders.filter(Payment_Status='Paid').count()
    
    # Add total_quantity to each order
    compost_orders_list = list(compost_orders)
    for order in compost_orders_list:
        total_qty = Decimal('0.00')
        for item in order.tbl_orderitem_set.all():
            total_qty += item.Quantity_kg
        order.total_quantity = total_qty
    
    context = {
        'orders': compost_orders_list,
        'status_filter': status_filter,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'pending_orders': pending_orders,
        'completed_orders': completed_orders,
    }
    return render(request, 'Admin/compost_sales.html', context)


@login_required(login_url='login')
@never_cache
def assign_waste_collector(request, order_id):
    """Admin assigns a collector to a waste order"""
    if request.method == 'POST':
        try:
            order = tbl_Order.objects.get(Order_id=order_id)
            collector_id = request.POST.get('collector_id')
            collector = Collector.objects.get(pk=collector_id)
            
            # Get order item
            order_item = order.tbl_orderitem_set.first()
            quantity = order_item.Quantity_kg
            unit_price = order_item.Unit_Price
            
            # Get any available inventory from this collector (just for linking)
            inventory = tbl_WasteInventory.objects.filter(
                collector=collector,
                is_available=True
            ).first()
            
            if not inventory:
                messages.error(request, f'{collector.collector_name} has no available inventory')
                return redirect('admin_waste_sales')
            
            # Create FarmerSupply (links farmer to collector)
            supply = tbl_FarmerSupply.objects.create(
                Farmer_id=order.Buyer_id,
                Collection_id=inventory.collection_request,
                Quantity=quantity,
                unit_price=unit_price,
                total_amount=order.Total_Amount,
                delivery_address=order.Delivery_Address,
                payment_status='Paid',
                delivery_status='Pending'
            )
            
            # Link to order item
            order_item.FarmerSupply_id = supply
            order_item.save()
            
            # NOTE: Stock is NOT deducted (per user requirement)
            # Inventory remains showing full available quantities
            
            # Update order assignment
            order.assigned_collector = collector
            order.assignment_status = 'Assigned'
            order.save()
            
            # Create payment transaction for the collector
            tbl_PaymentTransaction.objects.create(
                Payer_id=order.Buyer_id.user,
                Receiver_id=collector.user,
                Amount=order.Total_Amount,
                transaction_type='WasteSale',
                Reference_id=order.Order_id,
                status='Success'
            )
            
            messages.success(request, f'Order #{order_id} assigned to {collector.collector_name}')
        except Collector.DoesNotExist:
            messages.error(request, 'Collector not found')
        except Exception as e:
            messages.error(request, f'Error assigning collector: {str(e)}')
    
    return redirect('admin_waste_sales')


@login_required(login_url='login')
@never_cache
def admin_update_delivery_status(request, order_id):
    """Update delivery status for an order"""
    if request.method == 'POST':
        try:
            order = tbl_Order.objects.get(Order_id=order_id)
            new_status = request.POST.get('delivery_status')
            
            # Update all order items
            order.tbl_orderitem_set.all().update(Delivery_Status=new_status)

            # SYNC: Also update linked FarmerSupply records (for Waste Sales)
            # This ensures Collector view matches Admin view
            supply_ids = order.tbl_orderitem_set.filter(
                FarmerSupply_id__isnull=False
            ).values_list('FarmerSupply_id', flat=True)

            if supply_ids:
                waste_supplies = tbl_FarmerSupply.objects.filter(Supply_id__in=supply_ids)
                waste_supplies.update(delivery_status=new_status)

                # If Delivered, ensure Paid logic is consistent
                if new_status == 'Delivered':
                    waste_supplies.update(payment_status='Paid')
                    if order.Payment_Status != 'Paid':
                        order.Payment_Status = 'Paid'
                        order.save()
                        
                        # Update Transaction if exists
                        payment_transaction = tbl_PaymentTransaction.objects.filter(
                            Reference_id=order.Order_id,
                            transaction_type='WasteSale'
                        ).first()
                        if payment_transaction:
                            payment_transaction.status = 'Success'
                            payment_transaction.save()
            
            messages.success(request, f'Delivery status updated to {new_status}')
        except Exception as e:
            messages.error(request, f'Error updating status: {str(e)}')
    
    # Redirect back to appropriate page
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)
