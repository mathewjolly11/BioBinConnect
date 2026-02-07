from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from MyApp.models import tbl_Order, tbl_OrderItem, tbl_FarmerSupply, tbl_PaymentTransaction, tbl_WasteInventory, tbl_CompostBatch
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
        
    # Date Filtering
    date_filter = request.GET.get('period', '30')
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')
    
    start_date = None
    end_date = None
    
    from django.utils import timezone
    from datetime import datetime, timedelta
    
    if date_filter == 'custom' and start_date_str and end_date_str:
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d') + timedelta(days=1)
            waste_orders = waste_orders.filter(Order_Date__gte=start_date, Order_Date__lt=end_date)
        except ValueError:
            pass
    elif date_filter != 'all':
        try:
            days = int(date_filter)
            start_date = timezone.now() - timedelta(days=days)
            waste_orders = waste_orders.filter(Order_Date__gte=start_date)
        except (ValueError, TypeError):
             pass
             
    # Handle Export
    if request.GET.get('export') == 'excel':
        from MyApp.utils import generate_excel_report
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="Waste_Sales_{timezone.now().strftime("%Y-%m-%d")}.xlsx"'
        
        headers = ["Order ID", "Farmer", "Quantity (kg)", "Amount", "Payment Status", "Assignment", "Delivery", "Date"]
        data = []
        
        for order in waste_orders:
            # Calculate total qty manually since we can't always rely on annotations in all contexts
            total_qty = sum(item.Quantity_kg for item in order.tbl_orderitem_set.all())
            
            # Get delivery status
            item = order.tbl_orderitem_set.first()
            delivery_status = item.Delivery_Status if item else 'Pending'
            
            # Get collector name
            collector = order.assigned_collector.collector_name if order.assigned_collector else 'Unassigned'
            
            data.append([
                order.Order_id,
                order.Buyer_id.farmer_name,
                total_qty,
                order.Total_Amount,
                order.Payment_Status,
                collector,
                delivery_status,
                order.Order_Date.strftime('%Y-%m-%d')
            ])
            
        generate_excel_report(response, "Waste Sales Report", headers, data)
        return response
    
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
    
    # Get today's assigned collector for auto-assignment display
    todays_collector = get_todays_collector()
    from datetime import datetime
    day_name = datetime.now().strftime('%A')
    
    # Check if auto-assignment is enabled
    from MyApp.models import SystemSettings
    auto_assign_enabled = SystemSettings.get_setting('auto_assign_collectors', 'true').lower() == 'true'
    
    context = {
        'orders': waste_orders_list,
        'collectors': collectors,
        'todays_collector': todays_collector,
        'todays_collector_name': todays_collector.collector_name if todays_collector else 'None',
        'day_name': day_name,
        'auto_assign_enabled': auto_assign_enabled,
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
        
    # Date Filtering
    date_filter = request.GET.get('period', '30')
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')
    
    start_date = None
    end_date = None
    
    from django.utils import timezone
    from datetime import datetime, timedelta
    
    if date_filter == 'custom' and start_date_str and end_date_str:
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d') + timedelta(days=1)
            compost_orders = compost_orders.filter(Order_Date__gte=start_date, Order_Date__lt=end_date)
        except ValueError:
            pass
    elif date_filter != 'all':
        try:
            days = int(date_filter)
            start_date = timezone.now() - timedelta(days=days)
            compost_orders = compost_orders.filter(Order_Date__gte=start_date)
        except (ValueError, TypeError):
             pass
             
    # Handle Export
    if request.GET.get('export') == 'excel':
        from MyApp.utils import generate_excel_report
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="Compost_Sales_{timezone.now().strftime("%Y-%m-%d")}.xlsx"'
        
        headers = ["Order ID", "Buyer", "Quantity (packets)", "Amount", "Payment Status", "Date"]
        data = []
        
        for order in compost_orders:
            # Calculate total qty manually
            total_qty = sum(item.Quantity_kg for item in order.tbl_orderitem_set.all())
            
            data.append([
                order.Order_id,
                order.Buyer_id.user.name, # Buyer is CustomUser for compost
                int(total_qty), # Display as whole packets
                order.Total_Amount,
                order.Payment_Status,
                order.Order_Date.strftime('%Y-%m-%d')
            ])
            
        generate_excel_report(response, "Compost Sales Report", headers, data)
        return response
    
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




def get_todays_collector():
    """
    Get today's assigned collector based on day-of-week rotation.
    Rotates through all verified collectors automatically.
    Includes all 7 days (Monday-Sunday).
    """
    from datetime import datetime
    
    # Get all verified collectors in consistent order
    collectors = list(Collector.objects.filter(
        user__is_verified=True
    ).order_by('id'))
    
    if not collectors:
        return None
    
    # Get day of week (0=Monday, 6=Sunday)
    day_of_week = datetime.now().weekday()
    
    # Rotate through collectors based on day
    collector_index = day_of_week % len(collectors)
    
    return collectors[collector_index]


@login_required(login_url='login')
@never_cache
def auto_assign_waste_collector(request, order_id):
    """
    Auto-assign collector to farmer waste order using day-based rotation.
    All orders on the same day go to the same collector.
    """
    if request.method == 'POST':
        try:
            from datetime import datetime
            from django.http import JsonResponse
            
            order = tbl_Order.objects.get(Order_id=order_id)
            
            # Check if already assigned
            if order.assigned_collector:
                return JsonResponse({
                    'success': False,
                    'error': 'Order already has an assigned collector'
                })
            
            # Get today's assigned collector
            collector = get_todays_collector()
            
            if not collector:
                return JsonResponse({
                    'success': False,
                    'error': 'No verified collectors available'
                })
            
            # Get order item
            order_item = order.tbl_orderitem_set.first()
            quantity = order_item.Quantity_kg
            unit_price = order_item.Unit_Price
            
            # Get any available inventory from this collector (just for linking)
            inventory = tbl_WasteInventory.objects.filter(
                collector=collector,
                status='Available'
            ).first()
            
            # Allow assignment even without inventory
            collection_request = inventory.collection_request if inventory else None
            
            # Create FarmerSupply (links farmer to collector)
            supply = tbl_FarmerSupply.objects.create(
                Farmer_id=order.Buyer_id,
                Collection_id=collection_request,
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
            
            # Get day name for message
            day_name = datetime.now().strftime('%A')
            
            return JsonResponse({
                'success': True,
                'collector_name': collector.collector_name,
                'day': day_name,
                'message': f'Auto-assigned to {collector.collector_name} ({day_name}\'s collector)'
            })
            
        except tbl_Order.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': 'Order not found'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': f'Error: {str(e)}'
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@login_required(login_url='login')
@never_cache
def toggle_auto_assignment(request):
    """
    Toggle automatic collector assignment on/off.
    """
    if request.method == 'POST':
        from django.http import JsonResponse
        from MyApp.models import SystemSettings
        import json
        
        try:
            data = json.loads(request.body)
            enabled = data.get('enabled', False)
            
            # Update system setting
            SystemSettings.set_setting(
                'auto_assign_collectors',
                'true' if enabled else 'false',
                'Automatically assign collectors to farmer waste orders based on day rotation'
            )
            
            return JsonResponse({
                'success': True,
                'enabled': enabled,
                'message': f'Auto-assignment {"enabled" if enabled else "disabled"}'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


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
                status='Available'
            ).first()
            
            # Allow assignment even without inventory
            collection_request = inventory.collection_request if inventory else None
            
            # Create FarmerSupply (links farmer to collector)
            supply = tbl_FarmerSupply.objects.create(
                Farmer_id=order.Buyer_id,
                Collection_id=collection_request,
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


@login_required(login_url='login')
@never_cache
def admin_stock_management(request):
    """Admin view for stock management - shows waste inventory and compost stock"""
    
    # Get waste inventory data
    waste_inventory = tbl_WasteInventory.objects.select_related(
        'collection_request__household__user', 
        'collector__user'
    ).order_by('-collection_date')
    
    # Apply status filter for waste inventory
    waste_status_filter = request.GET.get('waste_status', 'all')
    if waste_status_filter != 'all':
        waste_inventory = waste_inventory.filter(status=waste_status_filter)
    
    # Add total value calculation to waste inventory
    waste_inventory_with_totals = []
    for item in waste_inventory:
        item.total_value = item.available_quantity_kg * item.price_per_kg
        waste_inventory_with_totals.append(item)
    
    # Get compost batch data
    from MyApp.models import tbl_CompostBatch
    compost_batches = tbl_CompostBatch.objects.select_related(
        'CompostManager_id__user'
    ).order_by('-Date_Created')
    
    # Apply status filter for compost batches
    compost_status_filter = request.GET.get('compost_status', 'all')
    if compost_status_filter != 'all':
        compost_batches = compost_batches.filter(Status=compost_status_filter)
    
    # Apply grade filter for compost batches
    grade_filter = request.GET.get('grade', 'all')
    if grade_filter != 'all':
        compost_batches = compost_batches.filter(Grade=grade_filter)
    
    # Add total value calculation to compost batches
    compost_batches_with_totals = []
    for batch in compost_batches:
        batch.total_value = batch.Stock_kg * batch.price_per_kg
        batch.stock_floored = int(batch.Stock_kg)  # Floor the stock value
        batch.source_floored = int(batch.Source_Waste_kg)  # Floor source waste
        compost_batches_with_totals.append(batch)
    
    # Calculate summary statistics
    waste_stats = {
        'total_available': waste_inventory.filter(status='Available').aggregate(
            total=Sum('available_quantity_kg'))['total'] or 0,
        'total_sold': waste_inventory.filter(status='Sold').aggregate(
            total=Sum('available_quantity_kg'))['total'] or 0,
        'total_composting': waste_inventory.filter(status='Composting').aggregate(
            total=Sum('available_quantity_kg'))['total'] or 0,
        'all_used': waste_inventory.filter(status='Used').aggregate(
            total=Sum('available_quantity_kg'))['total'] or 0,
    }
    
    compost_stats = {
        'total_active': compost_batches.filter(Status__in=['Active', 'Ready']).aggregate(
            total=Sum('Stock_kg'))['total'] or 0,
        'total_active_floored': int(compost_batches.filter(Status__in=['Active', 'Ready']).aggregate(
            total=Sum('Stock_kg'))['total'] or 0),
        'total_sold': compost_batches.filter(Status='Sold').aggregate(
            total=Sum('Stock_kg'))['total'] or 0,
        'premium_stock': compost_batches.filter(Grade='Premium', Status__in=['Active', 'Ready']).aggregate(
            total=Sum('Stock_kg'))['total'] or 0,
        'premium_stock_floored': int(compost_batches.filter(Grade='Premium', Status__in=['Active', 'Ready']).aggregate(
            total=Sum('Stock_kg'))['total'] or 0),
        'grade_a_stock': compost_batches.filter(Grade='A', Status__in=['Active', 'Ready']).aggregate(
            total=Sum('Stock_kg'))['total'] or 0,
        'grade_b_stock': compost_batches.filter(Grade='B', Status__in=['Active', 'Ready']).aggregate(
            total=Sum('Stock_kg'))['total'] or 0,
        'grade_c_stock': compost_batches.filter(Grade='C', Status__in=['Active', 'Ready']).aggregate(
            total=Sum('Stock_kg'))['total'] or 0,
    }
    
    # Calculate shortage against minimum total thresholds
    min_total_waste = 50  # Minimum 50kg total waste needed
    min_total_compost_packets = 50  # Minimum 50 compost packets needed
    
    # Calculate total available waste (only Available status)
    total_available_waste = waste_inventory.filter(
        status='Available'
    ).aggregate(total=Sum('available_quantity_kg'))['total'] or 0
    
    # Calculate total compost in packets (assuming 4kg per packet)
    total_compost_kg = compost_batches.filter(
        Status__in=['Active', 'Ready']
    ).aggregate(total=Sum('Stock_kg'))['total'] or 0
    
    compost_kg_per_packet = 1  # 1kg per packet
    total_compost_packets = total_compost_kg / compost_kg_per_packet
    
    # Calculate shortages
    waste_shortage = max(0, min_total_waste - total_available_waste)
    compost_packet_shortage = max(0, min_total_compost_packets - total_compost_packets)
    
    low_waste_stock = waste_shortage
    low_compost_stock = compost_packet_shortage
    
    context = {
        'waste_inventory': waste_inventory_with_totals,
        'compost_batches': compost_batches_with_totals,
        'waste_stats': waste_stats,
        'compost_stats': compost_stats,
        'low_waste_stock': low_waste_stock,
        'low_compost_stock': low_compost_stock,
        'waste_status_filter': waste_status_filter,
        'compost_status_filter': compost_status_filter,
        'grade_filter': grade_filter,
    }
    
    return render(request, 'Admin/stock_management.html', context)
