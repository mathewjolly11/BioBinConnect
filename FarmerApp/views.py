from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth import logout
from GuestApp.models import Farmer
from GuestApp.forms import FarmerEditForm, ProfileEditForm

@login_required(login_url='login')
@never_cache
def farmer_dashboard(request):
    return render(request, 'Farmer/index.html')

@login_required(login_url='login')
@never_cache
def farmer_profile(request):
    farmer = Farmer.objects.get(user=request.user)
    context = {
        'farmer': farmer,
        'user': request.user
    }
    return render(request, 'Farmer/profile.html', context)

@login_required(login_url='login')
@never_cache
def edit_profile(request):
    """Edit farmer profile"""
    farmer = Farmer.objects.get(user=request.user)
    
    if request.method == 'POST':
        user_form = ProfileEditForm(request.POST, instance=request.user)
        farmer_form = FarmerEditForm(request.POST, request.FILES, instance=farmer)
        
        if user_form.is_valid() and farmer_form.is_valid():
            user_form.save()
            farmer_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('farmer_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = ProfileEditForm(instance=request.user)
        farmer_form = FarmerEditForm(instance=farmer)
    
    context = {
        'user_form': user_form,
        'farmer_form': farmer_form,
        'farmer': farmer,
        'user': request.user
    }
    return render(request, 'Farmer/edit_profile.html', context)

@login_required(login_url='login')
@never_cache
def delete_account(request):
    """Delete farmer account permanently"""
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()  # This will cascade delete the farmer profile
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('login')
    
    return render(request, 'Farmer/delete_account_confirm.html')


# ============= FARMER WASTE PURCHASING SYSTEM =============

@login_required(login_url='login')
@never_cache
def farmer_browse_waste(request):
    """Browse available direct waste for animal feeding"""
    from MyApp.models import tbl_WasteInventory
    from django.db.models import Sum
    
    # Get all available waste and aggregate
    available_waste = tbl_WasteInventory.objects.filter(
        is_available=True,
        available_quantity_kg__gt=0,
        status='Available'
    )
    
    # Calculate totals
    total_stock = available_waste.aggregate(total=Sum('available_quantity_kg'))['total'] or 0
    batch_count = available_waste.count()
    
    context = {
        'total_stock': total_stock,
        'batch_count': batch_count,
        'has_stock': total_stock > 0
    }
    return render(request, 'Farmer/browse_waste.html', context)


@login_required(login_url='login')
@never_cache
def farmer_browse_compost(request):
    """Browse available processed compost for fertilizer"""
    from MyApp.models import tbl_CompostBatch
    from django.db.models import Sum
    
    # Get all available compost batches and aggregate total stock
    available_batches = tbl_CompostBatch.objects.filter(
        Stock_kg__gt=0,
        Status='Ready'
    )
    
    # Calculate total available stock across all batches
    total_stock = available_batches.aggregate(total=Sum('Stock_kg'))['total'] or 0
    batch_count = available_batches.count()
    
    # Get the most recent batch for display info
    latest_batch = available_batches.order_by('-Date_Created').first() if available_batches.exists() else None
    
    context = {
        'total_stock': total_stock,
        'batch_count': batch_count,
        'latest_batch': latest_batch,
        'has_stock': total_stock > 0
    }
    return render(request, 'Farmer/browse_compost.html', context)


@login_required(login_url='login')
@never_cache
def farmer_place_order(request):
    """Place order for waste or compost"""
    from MyApp.models import tbl_WasteInventory, tbl_CompostBatch, tbl_Order, tbl_OrderItem, tbl_FarmerSupply, tbl_PaymentTransaction
    from django.utils import timezone
    from decimal import Decimal
    
    if request.method == 'POST':
        farmer = Farmer.objects.get(user=request.user)
        order_type = request.POST.get('order_type')  # 'waste' or 'compost'
        item_id = request.POST.get('item_id')
        quantity = Decimal(request.POST.get('quantity'))
        delivery_address = request.POST.get('delivery_address')
        
        try:
            if order_type == 'waste':
                # Order direct waste
                inventory = tbl_WasteInventory.objects.get(Inventory_id=item_id)
                
                # Validate quantity
                if quantity > inventory.available_quantity_kg:
                    messages.error(request, f'Only {inventory.available_quantity_kg}kg available!')
                    return redirect('farmer_browse_waste')
                
                unit_price = inventory.price_per_kg
                total_amount = quantity * unit_price
                
                # Store order details in session for payment processing
                request.session['pending_order'] = {
                    'order_type': 'waste',
                    'item_id': item_id,
                    'quantity': str(quantity),
                    'delivery_address': delivery_address,
                    'total_amount': str(total_amount),
                    'unit_price': str(unit_price)
                }
                return redirect('farmer_payment')
                
            elif order_type == 'compost':
                # Order compost - handle both single batch and combined stock
                if item_id == 'all':
                    # Combined compost from all batches
                    from django.db.models import Sum
                    available_batches = tbl_CompostBatch.objects.filter(
                        Stock_kg__gt=0,
                        Status='Ready'
                    )
                    total_stock = available_batches.aggregate(total=Sum('Stock_kg'))['total'] or 0
                    
                    # Validate quantity
                    if quantity > total_stock:
                        messages.error(request, f'Only {total_stock}kg available!')
                        return redirect('farmer_browse_compost')
                    
                    unit_price = 200  # Fixed price
                else:
                    # Single batch order
                    batch = tbl_CompostBatch.objects.get(Batch_id=item_id)
                    
                    # Validate quantity
                    if quantity > batch.Stock_kg:
                        messages.error(request, f'Only {batch.Stock_kg}kg available!')
                        return redirect('farmer_browse_compost')
                    
                    unit_price = batch.price_per_kg
                
                total_amount = quantity * unit_price
                
                # Store order details in session for payment processing
                request.session['pending_order'] = {
                    'order_type': 'compost',
                    'item_id': item_id,
                    'quantity': str(quantity),
                    'delivery_address': delivery_address,
                    'total_amount': str(total_amount),
                    'unit_price': str(unit_price)
                }
                return redirect('farmer_payment')
                
        except Exception as e:
            messages.error(request, f'Error placing order: {str(e)}')
            return redirect('farmer_dashboard')
    
    # GET request - show order form
    order_type = request.GET.get('type')
    item_id = request.GET.get('id')
    
    if order_type == 'waste':
        if item_id == 'all':
            # Combined waste from all collections
            from django.db.models import Sum
            available_waste = tbl_WasteInventory.objects.filter(
                is_available=True,
                available_quantity_kg__gt=0,
                status='Available'
            )
            total_stock = available_waste.aggregate(total=Sum('available_quantity_kg'))['total'] or 0
            
            item_name = "Fresh Organic Waste for Animal Feed"
            available_qty = total_stock
            price = 10  # Fixed price ₹10/kg
            item_id = 'all'  # Keep as 'all' for processing
        else:
            item = tbl_WasteInventory.objects.get(Inventory_id=item_id)
            item_name = f"Direct Waste from {item.collector.collector_name}"
            available_qty = item.available_quantity_kg
            price = item.price_per_kg
    elif order_type == 'compost':
        if item_id == 'all':
            # Combined compost from all batches
            from django.db.models import Sum
            total_stock = tbl_CompostBatch.objects.filter(
                Stock_kg__gt=0,
                Status='Ready'
            ).aggregate(total=Sum('Stock_kg'))['total'] or 0
            
            item_name = "Premium Organic Compost - Grade A"
            available_qty = total_stock
            price = 200  # Fixed price
            item_id = 'all'  # Keep as 'all' for processing
        else:
            item = tbl_CompostBatch.objects.get(Batch_id=item_id)
            item_name = f"{item.Batch_name} - Standard Compost"
            available_qty = item.Stock_kg
            price = item.price_per_kg
    else:
        return redirect('farmer_dashboard')
    
    farmer = Farmer.objects.get(user=request.user)
    
    context = {
        'order_type': order_type,
        'item_id': item_id,
        'item_name': item_name,
        'available_qty': available_qty,
        'price': price,
        'farmer': farmer
    }
    return render(request, 'Farmer/place_order.html', context)


@login_required(login_url='login')
@never_cache
def farmer_orders(request):
    """View all orders placed by farmer"""
    from MyApp.models import tbl_Order
    from django.db.models import Sum
    
    farmer = Farmer.objects.get(user=request.user)
    orders = tbl_Order.objects.filter(Buyer_id=farmer).prefetch_related('tbl_orderitem_set').order_by('-Order_Date')
    
    # Calculate total spent
    total_spent = orders.aggregate(total=Sum('Total_Amount'))['total'] or 0
    
    context = {
        'orders': orders,
        'farmer': farmer,
        'total_spent': total_spent
    }
    return render(request, 'Farmer/orders.html', context)


@login_required(login_url='login')
@never_cache
def farmer_payment(request):
    """Process payment for farmer order"""
    from MyApp.models import tbl_WasteInventory, tbl_CompostBatch, tbl_Order, tbl_OrderItem, tbl_FarmerSupply, tbl_PaymentTransaction
    from decimal import Decimal
    from django.http import JsonResponse
    import json
    
    # Get pending order from session
    pending_order = request.session.get('pending_order')
    if not pending_order:
        messages.error(request, 'No pending order found.')
        return redirect('farmer_dashboard')
    
    # If GET request, show payment processing page
    if request.method == 'GET':
        context = {
            'order_details': pending_order
        }
        return render(request, 'Farmer/payment_processing.html', context)
    
    # If POST request, process the payment and create order
    farmer = Farmer.objects.get(user=request.user)
    
    # Get payment method from POST body
    try:
        body = json.loads(request.body)
        payment_method = body.get('payment_method', 'COD')
    except:
        payment_method = 'COD'
    
    order_type = pending_order['order_type']
    item_id = pending_order['item_id']
    quantity = Decimal(pending_order['quantity'])
    delivery_address = pending_order['delivery_address']
    total_amount = Decimal(pending_order['total_amount'])
    unit_price = Decimal(pending_order['unit_price'])
    
    try:
        if order_type == 'waste':
            inventory = tbl_WasteInventory.objects.get(Inventory_id=item_id)
            
            # Create FarmerSupply entry
            farmer_supply = tbl_FarmerSupply.objects.create(
                Farmer_id=farmer,
                Collection_id=inventory.collection_request,
                Quantity=quantity,
                unit_price=unit_price,
                total_amount=total_amount,
                delivery_address=delivery_address,
                payment_status='Paid',  # Payment completed
                delivery_status='Pending'
            )
            
            # Create Order
            order = tbl_Order.objects.create(
                Buyer_id=farmer,
                Total_Amount=total_amount,
                Delivery_Address=delivery_address,
                Payment_Status='Paid'  # Payment completed
            )
            
            # Create OrderItem
            tbl_OrderItem.objects.create(
                Order_id=order,
                Item_Type='Waste',
                FarmerSupply_id=farmer_supply,
                Quantity_kg=quantity,
                Unit_Price=unit_price,
                Delivery_Status='Pending'
            )
            
            # Update inventory
            inventory.available_quantity_kg -= quantity
            if inventory.available_quantity_kg == 0:
                inventory.status = 'Sold'
                inventory.is_available = False
            inventory.save()
            
            # Create payment transaction
            tbl_PaymentTransaction.objects.create(
                Payer_id=request.user,
                Receiver_id=inventory.collector.user,
                Amount=total_amount,
                transaction_type='WasteSale',
                Reference_id=order.Order_id,
                status='Success'  # Payment completed
            )
        
        elif order_type == 'compost':
            # Handle compost orders - both single batch and combined stock
            if item_id == 'all':
                # Combined compost from multiple batches
                # Create Order first
                order = tbl_Order.objects.create(
                    Buyer_id=farmer,
                    Total_Amount=total_amount,
                    Delivery_Address=delivery_address,
                    Payment_Status='Paid'
                )
                
                # Deduct from batches in order (FIFO)
                remaining_qty = quantity
                batches = tbl_CompostBatch.objects.filter(
                    Stock_kg__gt=0,
                    Status='Ready'
                ).order_by('Date_Created')
                
                for batch in batches:
                    if remaining_qty <= 0:
                        break
                    
                    deduct_qty = min(remaining_qty, batch.Stock_kg)
                    
                    # Create OrderItem for this batch
                    tbl_OrderItem.objects.create(
                        Order_id=order,
                        Item_Type='Compost',
                        Batch_id=batch,
                        Quantity_kg=deduct_qty,
                        Unit_Price=unit_price,
                        Delivery_Status='Pending'
                    )
                    
                    # Update batch stock
                    batch.Stock_kg -= deduct_qty
                    if batch.Stock_kg == 0:
                        batch.Status = 'Sold'
                    batch.save()
                    
                    remaining_qty -= deduct_qty
                
                # Create single payment transaction for combined order
                tbl_PaymentTransaction.objects.create(
                    Payer_id=request.user,
                    Receiver_id=request.user,  # Admin handles all sales
                    Amount=total_amount,
                    transaction_type='CompostSale',
                    Reference_id=order.Order_id,
                    status='Success'
                )
            else:
                # Single batch order
                batch = tbl_CompostBatch.objects.get(Batch_id=item_id)
                
                # Create Order
                order = tbl_Order.objects.create(
                    Buyer_id=farmer,
                    Total_Amount=total_amount,
                    Delivery_Address=delivery_address,
                    Payment_Status='Paid'
                )
                
                # Create OrderItem
                tbl_OrderItem.objects.create(
                    Order_id=order,
                    Item_Type='Compost',
                    Batch_id=batch,
                    Quantity_kg=quantity,
                    Unit_Price=unit_price,
                    Delivery_Status='Pending'
                )
                
                # Update batch stock
                batch.Stock_kg -= quantity
                if batch.Stock_kg == 0:
                    batch.Status = 'Sold'
                batch.save()
                
                # Create payment transaction
                tbl_PaymentTransaction.objects.create(
                    Payer_id=request.user,
                    Receiver_id=batch.CompostManager_id.user,
                    Amount=total_amount,
                    transaction_type='CompostSale',
                    Reference_id=order.Order_id,
                    status='Success'
                )
        
        # Clear session
        del request.session['pending_order']
        
        return JsonResponse({'success': True, 'order_id': order.Order_id})
        
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
