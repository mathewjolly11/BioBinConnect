@login_required(login_url='login')
@never_cache
def farmer_payment(request):
    """Process payment for farmer order"""
    from MyApp.models import tbl_WasteInventory, tbl_CompostBatch, tbl_Order, tbl_OrderItem, tbl_FarmerSupply, tbl_PaymentTransaction
    from decimal import Decimal
    
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
    order_type = pending_order['order_type']
    item_id = pending_order['item_id']
    quantity = Decimal(pending_order['quantity'])
    delivery_address = pending_order['delivery_address']
    payment_method = pending_order['payment_method']
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
        
        # Clear session
        del request.session['pending_order']
        
        return JsonResponse({'success': True, 'order_id': order.Order_id})
        
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
