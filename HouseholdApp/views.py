from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from GuestApp.models import Household
from GuestApp.forms import HouseholdEditForm, ProfileEditForm

@login_required(login_url='login')
@never_cache
def household_dashboard(request):
    from MyApp.models import tbl_PickupRequest, tbl_HouseholdPayment
    from django.db.models import Sum
    from django.utils import timezone
    from datetime import timedelta
    
    household = Household.objects.get(user=request.user)
    
    # Pickup requests summary
    total_requests = tbl_PickupRequest.objects.filter(household=household).count()
    pending_requests = tbl_PickupRequest.objects.filter(
        household=household, 
        status='Pending'
    ).count()
    completed_requests = tbl_PickupRequest.objects.filter(
        household=household, 
        status='Completed'
    ).count()
    
    # Next scheduled pickup
    next_pickup = tbl_PickupRequest.objects.filter(
        household=household,
        status__in=['Pending', 'Approved'],
        scheduled_date__gte=timezone.now().date()
    ).order_by('scheduled_date').first()
    
    # Payment summary (last 30 days)
    thirty_days_ago = timezone.now() - timedelta(days=30)
    total_paid = tbl_HouseholdPayment.objects.filter(
        household=household,
        payment_date__gte=thirty_days_ago
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    # All time payments
    total_paid_all_time = tbl_HouseholdPayment.objects.filter(
        household=household
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    # Recent payments
    recent_payments = tbl_HouseholdPayment.objects.filter(
        household=household
    ).order_by('-payment_date')[:5]
    
    # Recent requests
    recent_requests = tbl_PickupRequest.objects.filter(
        household=household
    ).order_by('-scheduled_date')[:5]
    
    context = {
        'household': household,
        'total_requests': total_requests,
        'pending_requests': pending_requests,
        'completed_requests': completed_requests,
        'next_pickup': next_pickup,
        'total_paid': total_paid,
        'total_paid_all_time': total_paid_all_time,
        'recent_payments': recent_payments,
        'recent_requests': recent_requests,
    }
    
    return render(request, 'HouseHold/index.html', context)

@login_required(login_url='login')
@never_cache
def household_profile(request):
    household = Household.objects.get(user=request.user)
    context = {
        'household': household,
        'user': request.user
    }
    return render(request, 'HouseHold/profile.html', context)

@login_required(login_url='login')
@never_cache
def edit_profile(request):
    """Edit household profile"""
    household = Household.objects.get(user=request.user)
    
    if request.method == 'POST':
        user_form = ProfileEditForm(request.POST, instance=request.user)
        household_form = HouseholdEditForm(request.POST, request.FILES, instance=household)
        
        if user_form.is_valid() and household_form.is_valid():
            user_form.save()
            household_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('household_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = ProfileEditForm(instance=request.user)
        household_form = HouseholdEditForm(instance=household)
    
    context = {
        'user_form': user_form,
        'household_form': household_form,
        'household': household,
        'user': request.user
    }
    return render(request, 'HouseHold/edit_profile.html', context)

@login_required(login_url='login')
@never_cache
def delete_account(request):
    """Delete household account permanently"""
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()  # This will cascade delete the household profile
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('login')
    
    return render(request, 'HouseHold/delete_account_confirm.html')

@login_required(login_url='login')
@never_cache
def request_pickup(request):
    from HouseholdApp.forms import PickupRequestForm
    from MyApp.models import tbl_Route, tbl_CollectorAssignment, tbl_HouseholdPayment
    from datetime import datetime
    from django.utils import timezone
    import time
    import random
    
    household = Household.objects.get(user=request.user)
    
    if request.method == 'POST':
        print("DEBUG: POST request received for pickup")
        form = PickupRequestForm(request.POST)
        print(f"DEBUG: Form valid: {form.is_valid()}, Errors: {form.errors}")
        if form.is_valid():
            scheduled_date = form.cleaned_data['scheduled_date']
            bin_type = form.cleaned_data['bin_type']
            payment_method = request.POST.get('payment_method', '')
            
            # Generate transaction ID
            transaction_id = f'TXN{int(time.time())}{random.randint(100, 999)}'
            
            # Create payment record in tbl_HouseholdPayment
            payment_record = tbl_HouseholdPayment.objects.create(
                household=household,
                bin_type=bin_type,
                amount=bin_type.price_rs,
                payment_for_date=scheduled_date,
                status='Completed',
                transaction_id=transaction_id
            )
            
            # Create pickup request
            req = form.save(commit=False)
            req.household = household
            req.status = 'Pending'  # Default status
            
            # Set payment details in pickup request
            req.payment_method = payment_method
            req.payment_amount = bin_type.price_rs
            req.payment_status = 'Completed'
            req.payment_date = timezone.now()
            req.transaction_id = transaction_id
            req.payment = payment_record  # Link to payment record
            
            # Logic to auto-assign collector based on Route/Range and Day
            collector_info = None
            warning_message = None
            
            if household.house_no is None:
                warning_message = "Please update your profile with your House Number to enable auto-assignment."
            else:
                # Find Route matching RA and House Range
                routes = tbl_Route.objects.filter(residents_association=household.residents_association)
                target_route = None
                
                for r in routes:
                    if r.start_house_no is not None and r.end_house_no is not None:
                        if r.start_house_no <= household.house_no <= r.end_house_no:
                            target_route = r
                            break
                
                if target_route:
                     # Find Assignment for the scheduled day
                     day_name = req.scheduled_date.strftime('%A')
                     
                     assignment = tbl_CollectorAssignment.objects.filter(Route_id=target_route, day_of_week=day_name).first()
                     
                     if assignment:
                         req.assigned_collector = assignment.collector
                         req.status = 'Approved'
                         collector_info = assignment.collector.collector_name
                     else:
                         warning_message = f"No collector is explicitly assigned to your route ({target_route.name}) on {day_name}. Status is Pending."
                else:
                    warning_message = "Your house is not currently mapped to a specific pickup route. Admin will review."
            
            req.save()
            
            # Initialize email status tracking
            email_status = {
                'household_confirmation': False,
                'collector_assignment': False,
                'pickup_scheduled': False,
                'errors': []
            }
            
            # Send pickup confirmation email to household
            try:
                from utils.email_service import send_pickup_confirmation_email
                email_status['household_confirmation'] = send_pickup_confirmation_email(req)
                if not email_status['household_confirmation']:
                    email_status['errors'].append('Failed to send confirmation email to household')
            except Exception as e:
                print(f"Household confirmation email failed: {e}")
                email_status['errors'].append(f'Household email error: {str(e)}')
            
            # If collector was assigned, send notification emails
            if req.assigned_collector:
                try:
                    from utils.email_service import send_pickup_assignment_email, send_pickup_scheduled_email
                    email_status['collector_assignment'] = send_pickup_assignment_email(req)  # To collector
                    email_status['pickup_scheduled'] = send_pickup_scheduled_email(req)   # To household
                    
                    if not email_status['collector_assignment']:
                        email_status['errors'].append('Failed to send assignment email to collector')
                    if not email_status['pickup_scheduled']:
                        email_status['errors'].append('Failed to send scheduled notification to household')
                        
                except Exception as e:
                    print(f"Collector/Scheduled email notification failed: {e}")
                    email_status['errors'].append(f'Collector notification error: {str(e)}')
            
            # Check if this is an AJAX request
            if request.headers.get('Content-Type') == 'application/json':
                # Return JSON response for AJAX
                response_data = {
                    'success': True,
                    'message': 'Pickup request created successfully!',
                    'pickup_data': {
                        'amount': str(req.payment_amount),
                        'transaction_id': req.transaction_id,
                        'date': str(req.scheduled_date),
                        'payment_method': req.payment_method,
                        'collector': collector_info,
                        'warning': warning_message
                    },
                    'email_status': email_status
                }
                return JsonResponse(response_data)
            
            # Store success message in session for regular form submission
            request.session['pickup_success'] = {
                'amount': str(req.payment_amount),
                'transaction_id': req.transaction_id,
                'date': str(req.scheduled_date),
                'payment_method': req.payment_method,
                'collector': collector_info,
                'warning': warning_message,
                'email_status': email_status
            }
            
            return redirect('view_requests')
        else:
            # Form is not valid - show errors with SweetAlert
            error_list = []
            for field, errors in form.errors.items():
                for error in errors:
                    error_list.append(f'{field}: {error}')
            
            # Check if this is an AJAX request
            if request.headers.get('Content-Type') == 'application/json':
                return JsonResponse({
                    'success': False,
                    'message': 'Form validation failed',
                    'errors': error_list
                })
            
            # Add errors to Django messages for display
            for error in error_list:
                messages.error(request, error)
    else:
        form = PickupRequestForm()
    
    context = {'form': form}
    return render(request, 'HouseHold/request_pickup.html', context)

@login_required(login_url='login')
@never_cache
def view_requests(request):
    from MyApp.models import tbl_PickupRequest
    household = Household.objects.get(user=request.user)
    requests = tbl_PickupRequest.objects.filter(household=household).order_by('-scheduled_date')
    
    # Clear the success message after displaying
    if 'pickup_success' in request.session:
        del request.session['pickup_success']
    
    return render(request, 'HouseHold/view_requests.html', {'requests': requests})

@login_required(login_url='login')
@never_cache
def make_payment(request):
    """Allow household to make payment for waste pickup service"""
    from HouseholdApp.forms import PaymentForm
    from MyApp.models import tbl_HouseholdPayment
    import time
    import random
    
    household = Household.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.household = household
            payment.amount = payment.bin_type.price_rs  # Set amount based on bin type
            payment.status = 'Completed'
            # Generate transaction ID
            payment.transaction_id = f'TXN{int(time.time())}{random.randint(100, 999)}'
            payment.save()
            
            messages.success(request, f'Payment of ₹{payment.amount} completed successfully for {payment.payment_for_date}! Transaction ID: {payment.transaction_id}')
            return redirect('household_dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = PaymentForm()
    
    return render(request, 'HouseHold/make_payment.html', {'form': form})

@login_required(login_url='login')
@never_cache
def payment_history(request):
    """Display payment history for the household"""
    from MyApp.models import tbl_HouseholdPayment
    
    household = Household.objects.get(user=request.user)
    payments = tbl_HouseholdPayment.objects.filter(household=household).order_by('-payment_date')
    
    return render(request, 'HouseHold/payment_history.html', {'payments': payments})

@login_required(login_url='login')
@never_cache
def services(request):
    """Display services page for households"""
    household = Household.objects.get(user=request.user)
    return render(request, 'HouseHold/services.html', {'household': household})

@login_required(login_url='login')
@never_cache
@csrf_exempt
def request_pickup_ajax(request):
    """AJAX endpoint for pickup requests with email status tracking"""
    from HouseholdApp.forms import PickupRequestForm
    from MyApp.models import tbl_Route, tbl_CollectorAssignment, tbl_HouseholdPayment
    from datetime import datetime
    from django.utils import timezone
    import time
    import random
    
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
    
    try:
        # Parse JSON data
        data = json.loads(request.body)
        household = Household.objects.get(user=request.user)
        
        # Create form instance with the data
        form = PickupRequestForm(data)
        
        if form.is_valid():
            scheduled_date = form.cleaned_data['scheduled_date']
            bin_type = form.cleaned_data['bin_type']
            payment_method = data.get('payment_method', '')
            
            # Generate transaction ID
            transaction_id = f'TXN{int(time.time())}{random.randint(100, 999)}'
            
            # Create payment record in tbl_HouseholdPayment
            payment_record = tbl_HouseholdPayment.objects.create(
                household=household,
                bin_type=bin_type,
                amount=bin_type.price_rs,
                payment_for_date=scheduled_date,
                status='Completed',
                transaction_id=transaction_id
            )
            
            # Create pickup request
            req = form.save(commit=False)
            req.household = household
            req.status = 'Pending'  # Default status
            
            # Set payment details in pickup request
            req.payment_method = payment_method
            req.payment_amount = bin_type.price_rs
            req.payment_status = 'Completed'
            req.payment_date = timezone.now()
            req.transaction_id = transaction_id
            req.payment = payment_record  # Link to payment record
            
            # Logic to auto-assign collector based on Route/Range and Day
            collector_info = None
            warning_message = None
            
            if household.house_no is None:
                warning_message = "Please update your profile with your House Number to enable auto-assignment."
            else:
                # Find Route matching RA and House Range
                routes = tbl_Route.objects.filter(residents_association=household.residents_association)
                target_route = None
                
                for r in routes:
                    if r.start_house_no is not None and r.end_house_no is not None:
                        if r.start_house_no <= household.house_no <= r.end_house_no:
                            target_route = r
                            break
                
                if target_route:
                     # Find Assignment for the scheduled day
                     day_name = req.scheduled_date.strftime('%A')
                     
                     assignment = tbl_CollectorAssignment.objects.filter(Route_id=target_route, day_of_week=day_name).first()
                     
                     if assignment:
                         req.assigned_collector = assignment.collector
                         req.status = 'Approved'
                         collector_info = assignment.collector.collector_name
                     else:
                         warning_message = f"No collector is explicitly assigned to your route ({target_route.name}) on {day_name}. Status is Pending."
                else:
                    warning_message = "Your house is not currently mapped to a specific pickup route. Admin will review."
            
            req.save()
            
            # Initialize email status tracking
            email_status = {
                'household_confirmation': False,
                'collector_assignment': False,
                'pickup_scheduled': False,
                'errors': []
            }
            
            # Send pickup confirmation email to household
            try:
                from utils.email_service import send_pickup_confirmation_email
                email_status['household_confirmation'] = send_pickup_confirmation_email(req)
                if not email_status['household_confirmation']:
                    email_status['errors'].append('Failed to send confirmation email to household')
            except Exception as e:
                print(f"Household confirmation email failed: {e}")
                email_status['errors'].append(f'Household email error: {str(e)}')
            
            # If collector was assigned, send notification emails
            if req.assigned_collector:
                try:
                    from utils.email_service import send_pickup_assignment_email, send_pickup_scheduled_email
                    email_status['collector_assignment'] = send_pickup_assignment_email(req)  # To collector
                    email_status['pickup_scheduled'] = send_pickup_scheduled_email(req)   # To household
                    
                    if not email_status['collector_assignment']:
                        email_status['errors'].append('Failed to send assignment email to collector')
                    if not email_status['pickup_scheduled']:
                        email_status['errors'].append('Failed to send scheduled notification to household')
                        
                except Exception as e:
                    print(f"Collector/Scheduled email notification failed: {e}")
                    email_status['errors'].append(f'Collector notification error: {str(e)}')
            
            # Return JSON response
            response_data = {
                'success': True,
                'message': 'Pickup request created successfully!',
                'pickup_data': {
                    'amount': str(req.payment_amount),
                    'transaction_id': req.transaction_id,
                    'date': str(req.scheduled_date),
                    'payment_method': req.payment_method,
                    'collector': collector_info,
                    'warning': warning_message,
                    'pickup_id': req.Pickup_id
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
def contact(request):
    """Display contact page for households"""
    household = Household.objects.get(user=request.user)
    return render(request, 'HouseHold/contact.html', {'household': household})


