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
