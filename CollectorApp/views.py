from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from GuestApp.models import Collector
from GuestApp.forms import CollectorEditForm, ProfileEditForm
from django.db.models import Q

@login_required(login_url='login')
@never_cache
def collector_dashboard(request):
    from MyApp.models import tbl_PickupRequest, tbl_CollectionRequest, tbl_WasteInventory, tbl_FarmerSupply, tbl_Order
    from django.db.models import Sum
    from django.utils import timezone
    from datetime import timedelta
    
    collector = Collector.objects.get(user=request.user)
    
    # Today's pickups (only pending/active ones)
    today = timezone.now().date()
    today_pickups = tbl_PickupRequest.objects.filter(
        assigned_collector=collector,
        scheduled_date=today,
        status__in=['Assigned', 'Pending', 'Scheduled', 'Approved']  # Include Approved status
    )
    today_pickups_count = today_pickups.count()
    
    # This month's collections
    month_start = timezone.now().replace(day=1)
    collections_this_month = tbl_CollectionRequest.objects.filter(
        collector=collector,
        collection_date__gte=month_start
    ).count()
    
    # Total waste collected (this month)
    waste_collected = tbl_CollectionRequest.objects.filter(
        collector=collector,
        collection_date__gte=month_start
    ).aggregate(total=Sum('total_quantity_kg'))['total'] or 0
    
    # All time collections
    total_collections = tbl_CollectionRequest.objects.filter(
        collector=collector
    ).count()
    
    # Waste inventory (available for farmers)
    available_waste = tbl_WasteInventory.objects.filter(
        collector=collector,
        status='Available'
    ).aggregate(total=Sum('available_quantity_kg'))['total'] or 0
    
    # Pending deliveries
    # Pending deliveries - check both direct collection and order assignment
    pending_deliveries = tbl_FarmerSupply.objects.filter(
        Q(Collection_id__collector=collector) | 
        Q(tbl_orderitem__Order_id__assigned_collector=collector),
        delivery_status='Pending'
    ).distinct().count()
    
    # Recent collections
    recent_collections = tbl_CollectionRequest.objects.filter(
        collector=collector
    ).order_by('-collection_date')[:5]
    
    # Assigned waste delivery orders (Sales)
    assigned_sales_orders = tbl_Order.objects.filter(
        assigned_collector=collector,
        assignment_status='Assigned',
        tbl_orderitem__Delivery_Status__in=['Pending', 'Dispatched']
    ).distinct().order_by('Order_Date')
    
    context = {
        'collector': collector,
        'today_pickups': today_pickups,
        'today_pickups_count': today_pickups_count,
        'assigned_sales_orders': assigned_sales_orders, # Added this
        'collections_this_month': collections_this_month,
        'waste_collected': waste_collected,
        'total_collections': total_collections,
        'available_waste': available_waste,
        'pending_deliveries': pending_deliveries,
        'recent_collections': recent_collections,
    }
    
    return render(request, 'Collector/index.html', context)

@login_required(login_url='login')
@never_cache
def collector_profile(request):
    collector = Collector.objects.get(user=request.user)
    context = {
        'collector': collector,
        'user': request.user
    }
    return render(request, 'Collector/profile.html', context)

@login_required(login_url='login')
@never_cache
def edit_profile(request):
    """Edit collector profile"""
    collector = Collector.objects.get(user=request.user)
    
    if request.method == 'POST':
        user_form = ProfileEditForm(request.POST, instance=request.user)
        collector_form = CollectorEditForm(request.POST, request.FILES, instance=collector)
        
        if user_form.is_valid() and collector_form.is_valid():
            user_form.save()
            collector_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('collector_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = ProfileEditForm(instance=request.user)
        collector_form = CollectorEditForm(instance=collector)
    
    context = {
        'user_form': user_form,
        'collector_form': collector_form,
        'collector': collector,
        'user': request.user
    }
    return render(request, 'Collector/edit_profile.html', context)

@login_required(login_url='login')
@never_cache
def delete_account(request):
    """Delete collector account permanently"""
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()  # This will cascade delete the collector profile
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('login')
    
    return render(request, 'Collector/delete_account_confirm.html')

@login_required(login_url='login')
@never_cache
def view_assigned_pickups(request):
    from MyApp.models import tbl_PickupRequest
    collector = Collector.objects.get(user=request.user)
    
    # Filter for requests assigned to this collector that are NOT completed
    # Showing Approved (Upcoming) and Pending (if manually assigned)
    assignments = tbl_PickupRequest.objects.filter(
        assigned_collector=collector
    ).exclude(status='Completed').order_by('scheduled_date')
    
    return render(request, 'Collector/assigned_pickups.html', {'assignments': assignments})

@login_required(login_url='login')
@never_cache
def log_collection(request, pickup_id):
    from MyApp.models import tbl_PickupRequest, tbl_CollectionRequest, tbl_WasteInventory
    from CollectorApp.forms import CollectionLogForm
    from django.utils import timezone
    
    pickup_request = tbl_PickupRequest.objects.get(Pickup_id=pickup_id)
    collector = Collector.objects.get(user=request.user)
    
    # Security check: Ensure this pickup is assigned to the current collector
    if pickup_request.assigned_collector != collector:
        messages.error(request, "You are not authorized to log this collection.")
        return redirect('collector_dashboard')

    if request.method == 'POST':
        form = CollectionLogForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.household = pickup_request.household
            collection.collector = collector
            collection.collection_date = timezone.now()
            collection.status = 'Collected'
            
            # Keep as 0 initially - will be updated when farmers purchase or compost manager collects
            collection.farmer_supply_kg = 0
            collection.leftover_compost_kg = 0
            
            collection.save()
            
            # Create waste inventory for farmer purchasing
            from MyApp.models import SystemSettings
            default_price = float(SystemSettings.get_setting('waste_price_per_kg', '10.00'))
            
            waste_inventory = tbl_WasteInventory.objects.create(
                collection_request=collection,
                collector=collector,
                available_quantity_kg=collection.total_quantity_kg,
                price_per_kg=default_price,  # Get price from system settings
                collection_date=timezone.now(),
                status='Available'
            )
            
            # Update Pickup Request status AND actual weight
            pickup_request.status = 'Completed'
            pickup_request.actual_weight_kg = collection.total_quantity_kg  # Save actual weight
            pickup_request.save()
            
            # Initialize email status tracking
            email_status = {
                'household_completion': False,
                'admin_notification': False,
                'farmer_notification': False,
                'errors': []
            }
            
            # Send collection completed email to household
            try:
                from utils.email_service import send_collection_completed_email
                from django.conf import settings
                
                # Check if household has a valid email
                household_email = pickup_request.household.user.email
                if not household_email or '@' not in household_email:
                    email_status['errors'].append(f'Household has invalid email address: {household_email}')
                    print(f"❌ Invalid household email: {household_email}")
                else:
                    email_status['household_completion'] = send_collection_completed_email(collection, pickup_request)
                    if email_status['household_completion']:
                        # Email sent successfully  
                        if settings.EMAIL_BACKEND == 'django.core.mail.backends.console.EmailBackend':
                            print(f"✅ Collection completion email logged to console for {household_email}")
                        else:
                            print(f"✅ Collection completion email sent to {household_email}")
                    else:
                        if settings.EMAIL_BACKEND == 'django.core.mail.backends.console.EmailBackend':
                            email_status['errors'].append('Email logged to console (development mode)')
                        else:
                            email_status['errors'].append('Failed to send completion email (Gmail sending limit may be exceeded)')
                            
            except Exception as e:
                error_msg = str(e)
                print(f"❌ Household completion email failed: {e}")
                
                if "Daily user sending limit exceeded" in error_msg:
                    email_status['errors'].append('Gmail daily sending limit exceeded - emails will resume tomorrow')
                elif "Authentication failed" in error_msg:
                    email_status['errors'].append('Email authentication failed - check Gmail credentials')
                else:
                    email_status['errors'].append(f'Email system error: {str(e)}')
            
            # Check if this is an AJAX request
            if request.headers.get('Content-Type') == 'application/json':
                # Return JSON response for AJAX
                response_data = {
                    'success': True,
                    'message': 'Collection logged successfully!',
                    'collection_data': {
                        'pickup_id': pickup_request.Pickup_id,
                        'weight': str(collection.total_quantity_kg),
                        'collection_date': str(collection.collection_date.strftime('%Y-%m-%d %H:%M')),
                        'household_name': pickup_request.household.household_name,
                        'inventory_id': waste_inventory.Inventory_id
                    },
                    'email_status': email_status
                }
                return JsonResponse(response_data)
            
            messages.success(request, f"Collection logged successfully! {collection.total_quantity_kg} kg now available for farmer purchase.")
            return redirect('view_assigned_pickups')
    else:
        form = CollectionLogForm()
    
    # Get current waste price for display
    from MyApp.models import SystemSettings
    current_waste_price = SystemSettings.get_setting('waste_price_per_kg', '10.00')
    
    return render(request, 'Collector/log_collection.html', {
        'form': form, 
        'pickup': pickup_request,
        'current_waste_price': current_waste_price
    })

@login_required(login_url='login')
@never_cache
@csrf_exempt
def log_collection_ajax(request, pickup_id):
    """AJAX endpoint for collection logging with email status tracking"""
    from MyApp.models import tbl_PickupRequest, tbl_CollectionRequest, tbl_WasteInventory
    from CollectorApp.forms import CollectionLogForm
    from django.utils import timezone
    
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
    
    try:
        # Parse JSON data
        data = json.loads(request.body)
        pickup_request = tbl_PickupRequest.objects.get(Pickup_id=pickup_id)
        collector = Collector.objects.get(user=request.user)
        
        # Security check: Ensure this pickup is assigned to the current collector
        if pickup_request.assigned_collector != collector:
            return JsonResponse({
                'success': False,
                'message': 'You are not authorized to log this collection.'
            })

        # Create form instance with the data
        form = CollectionLogForm(data)
        
        if form.is_valid():
            collection = form.save(commit=False)
            collection.household = pickup_request.household
            collection.collector = collector
            collection.collection_date = timezone.now()
            collection.status = 'Collected'
            
            # Keep as 0 initially - will be updated when farmers purchase or compost manager collects
            collection.farmer_supply_kg = 0
            collection.leftover_compost_kg = 0
            
            collection.save()
            
            # Create waste inventory for farmer purchasing
            from MyApp.models import SystemSettings
            default_price = float(SystemSettings.get_setting('waste_price_per_kg', '10.00'))
            
            waste_inventory = tbl_WasteInventory.objects.create(
                collection_request=collection,
                collector=collector,
                available_quantity_kg=collection.total_quantity_kg,
                price_per_kg=default_price,  # Get price from system settings
                collection_date=timezone.now(),
                status='Available'
            )
            
            # Update Pickup Request status AND actual weight
            pickup_request.status = 'Completed'
            pickup_request.actual_weight_kg = collection.total_quantity_kg  # Save actual weight
            pickup_request.save()
            
            # Initialize email status tracking
            email_status = {
                'household_completion': False,
                'admin_notification': False,
                'farmer_notification': False,
                'errors': []
            }
            
            # Send collection completed email to household
            try:
                from utils.email_service import send_collection_completed_email
                from django.conf import settings
                from MyApp.models import SystemSettings
                
                # Check system setting
                email_enabled = SystemSettings.get_setting('email_notifications_enabled', 'True')

                if email_enabled == 'False':
                    email_status['household_completion'] = 'Skipped'
                else:
                    # Check if household has a valid email
                    household_email = pickup_request.household.user.email
                    if not household_email or '@' not in household_email:
                        email_status['errors'].append(f'Household has invalid email address: {household_email}')
                        print(f"❌ Invalid household email: {household_email}")
                    else:
                        email_status['household_completion'] = send_collection_completed_email(collection, pickup_request)
                        if email_status['household_completion']:
                            # Email sent successfully  
                            if settings.EMAIL_BACKEND == 'django.core.mail.backends.console.EmailBackend':
                                print(f"✅ Collection completion email logged to console for {household_email}")
                            else:
                                print(f"✅ Collection completion email sent to {household_email}")
                        else:
                            if settings.EMAIL_BACKEND == 'django.core.mail.backends.console.EmailBackend':
                                email_status['errors'].append('Email logged to console (development mode)')
                            else:
                                email_status['errors'].append('Failed to send completion email (Gmail sending limit may be exceeded)')
                            
            except Exception as e:
                error_msg = str(e)
                print(f"❌ Household completion email failed: {e}")
                
                if "Daily user sending limit exceeded" in error_msg:
                    email_status['errors'].append('Gmail daily sending limit exceeded - emails will resume tomorrow')
                elif "Authentication failed" in error_msg:
                    email_status['errors'].append('Email authentication failed - check Gmail credentials')
                else:
                    email_status['errors'].append(f'Email system error: {str(e)}')
            
            # Return JSON response
            response_data = {
                'success': True,
                'message': 'Collection logged successfully!',
                'collection_data': {
                    'pickup_id': pickup_request.Pickup_id,
                    'weight': str(collection.total_quantity_kg),
                    'collection_date': str(collection.collection_date.strftime('%Y-%m-%d %H:%M')),
                    'household_name': pickup_request.household.household_name,
                    'inventory_id': waste_inventory.Inventory_id,
                    'collection_id': collection.Request_id
                },
                'email_status': email_status
            }
            return JsonResponse(response_data)
            
        else:
            # Form is not valid
            error_list = []
            for field, errors in form.errors.items():
                for error in errors:
                    error_list.append(f'{field}: {error}')
            
            return JsonResponse({
                'success': False,
                'message': 'Form validation failed',
                'errors': error_list
            })
            
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Server error: {str(e)}',
            'errors': [str(e)]
        })
@login_required(login_url='login')
@never_cache
def collection_history(request):
    from MyApp.models import tbl_CollectionRequest
    collector = Collector.objects.get(user=request.user)
    
    history = tbl_CollectionRequest.objects.filter(collector=collector).order_by('-collection_date')
    return render(request, 'Collector/collection_history.html', {'history': history})


@login_required(login_url='login')
@never_cache
def collector_waste_inventory(request):
    """View waste inventory with farmer purchase tracking"""
    from MyApp.models import tbl_WasteInventory
    collector = Collector.objects.get(user=request.user)
    
    # Get all waste inventory entries for this collector
    inventory_list = tbl_WasteInventory.objects.filter(
        collector=collector
    ).select_related('collection_request').order_by('-collection_date')
    
    # Calculate sold amounts for each inventory
    for inventory in inventory_list:
        total_collected = inventory.collection_request.total_quantity_kg
        remaining = inventory.available_quantity_kg
        sold_to_farmers = total_collected - remaining
        
        inventory.sold_amount = sold_to_farmers
        inventory.percentage_sold = (sold_to_farmers / total_collected * 100) if total_collected > 0 else 0
        inventory.percentage_remaining = (remaining / total_collected * 100) if total_collected > 0 else 0
    
    context = {
        'inventory_list': inventory_list,
        'collector': collector
    }
    return render(request, 'Collector/waste_inventory.html', context)


@login_required(login_url='login')
@never_cache
def collector_sales_orders(request):
    """View farmer orders for collector's waste"""
    from MyApp.models import tbl_FarmerSupply, tbl_PaymentTransaction
    collector = Collector.objects.get(user=request.user)
    
    # Get all farmer supplies from this collector's waste (direct or assigned)
    sales = tbl_FarmerSupply.objects.filter(
        Q(Collection_id__collector=collector) | 
        Q(tbl_orderitem__Order_id__assigned_collector=collector)
    ).select_related('Farmer_id', 'Collection_id').distinct().order_by('-Supply_Date')
    
    context = {
        'sales': sales,
        'collector': collector
    }
    return render(request, 'Collector/sales_orders.html', context)


@login_required(login_url='login')
@never_cache
def update_delivery_status(request, supply_id):
    """Update delivery status for a farmer supply order"""
    from MyApp.models import tbl_FarmerSupply, tbl_OrderItem
    
    collector = Collector.objects.get(user=request.user)
    
    try:
        supply = tbl_FarmerSupply.objects.get(
            Q(Supply_id=supply_id) & 
            (Q(Collection_id__collector=collector) | Q(tbl_orderitem__Order_id__assigned_collector=collector))
        )
        
        # Update delivery status based on current status
        if supply.delivery_status == 'Pending':
            supply.delivery_status = 'Dispatched'
            
            # Also update OrderItem delivery status
            order_item = tbl_OrderItem.objects.filter(FarmerSupply_id=supply).first()
            if order_item:
                order_item.Delivery_Status = 'Dispatched'
                order_item.save()
            
            messages.success(request, f'Order #{supply_id} marked as Dispatched!')
            
        elif supply.delivery_status == 'Dispatched':
            supply.delivery_status = 'Delivered'
            
            # Use 'Paid' for all completed deliveries (User Requirement: Treat all as Paid)
            if supply.payment_status != 'Paid':
                supply.payment_status = 'Paid'
                
                # Also update Order payment status
                order_item = tbl_OrderItem.objects.filter(FarmerSupply_id=supply).first()
                if order_item:
                    order = order_item.Order_id
                    # Only update Order to Paid if not already (though likely is)
                    if order.Payment_Status != 'Paid':
                        order.Payment_Status = 'Paid'
                        order.save()
                    
                    # Update PaymentTransaction status
                    from MyApp.models import tbl_PaymentTransaction
                    payment_transaction = tbl_PaymentTransaction.objects.filter(
                        Reference_id=order.Order_id,
                        transaction_type='WasteSale'
                    ).first()
                    if payment_transaction:
                        payment_transaction.status = 'Success'
                        payment_transaction.save()
            
            # Also update OrderItem delivery status
            order_item = tbl_OrderItem.objects.filter(FarmerSupply_id=supply).first()
            if order_item:
                order_item.Delivery_Status = 'Delivered'
                order_item.save()
            
            messages.success(request, f'Order #{supply_id} marked as Delivered!')
        
        supply.save()
        
    except tbl_FarmerSupply.DoesNotExist:
        messages.error(request, 'Order not found or unauthorized access.')
    
    return redirect('collector_sales_orders')

def services(request):
    """Display services page for collectors"""
    collector = Collector.objects.get(user=request.user)
    return render(request, 'Collector/services.html', {'collector': collector})

def contact(request):
    """Display contact page for collectors"""
    collector = Collector.objects.get(user=request.user)
    return render(request, 'Collector/contact.html', {'collector': collector})

def about_us(request):
    """Display about page for collectors"""
    collector = Collector.objects.get(user=request.user)
    return render(request, 'Collector/about.html', {'collector': collector})
