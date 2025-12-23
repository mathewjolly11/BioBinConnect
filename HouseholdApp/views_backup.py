from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth import logout
from GuestApp.models import Household
from GuestApp.forms import HouseholdEditForm, ProfileEditForm

@login_required(login_url='login')
@never_cache
def household_dashboard(request):
    return render(request, 'HouseHold/index.html')

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
    
    household = Household.objects.get(user=request.user)
    
    if request.method == 'POST':
        print("DEBUG: POST request received for pickup")
        form = PickupRequestForm(request.POST)
        print(f"DEBUG: Form valid: {form.is_valid()}, Errors: {form.errors}")
        if form.is_valid():
            scheduled_date = form.cleaned_data['scheduled_date']
            bin_type = form.cleaned_data['bin_type']
            
            # Check if payment exists for this date
            payment = tbl_HouseholdPayment.objects.filter(
                household=household,
                payment_for_date=scheduled_date,
                status='Completed'
            ).first()
            
            if not payment:
                messages.error(request, f'Payment required! Please make payment for {scheduled_date} before requesting pickup.')
                return redirect('make_payment')
            
            # Verify bin type matches payment
            if payment.bin_type != bin_type:
                messages.error(request, f'Bin type mismatch! You paid for {payment.bin_type.name} bin but selected {bin_type.name} bin.')
                return redirect('request_pickup')
            
            req = form.save(commit=False)
            req.household = household
            req.payment = payment
            
            # Logic to auto-assign collector based on Route/Range and Day
            if household.house_no is None:
                messages.error(request, "Please update your profile with your House Number to enable auto-assignment.")
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
                         messages.success(request, f"Pickup request submitted successfully! Assigned to {assignment.collector.collector_name}.")
                     else:
                         messages.warning(request, f"Request submitted. No collector is explicitly assigned to your route ({target_route.name}) on {day_name}. Status is Pending.")
                else:
                    messages.warning(request, "Request submitted. Your house is not currently mapped to a specific pickup route. Admin will review.")
            
            print(f"DEBUG: Saving pickup request for household {household}")
            req.save()
            print(f"DEBUG: Pickup request saved! ID: {req.Pickup_id}")
            messages.success(request, 'Pickup request created successfully!')
            return redirect('view_requests')
        else:
            # Form is not valid - show errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = PickupRequestForm()
    
    return render(request, 'HouseHold/request_pickup.html', {'form': form})

@login_required(login_url='login')
@never_cache
def view_requests(request):
    from MyApp.models import tbl_PickupRequest
    household = Household.objects.get(user=request.user)
    requests = tbl_PickupRequest.objects.filter(household=household).order_by('-scheduled_date')
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


