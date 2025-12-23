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
    from MyApp.models import tbl_Route, tbl_CollectorAssignment
    
    household = Household.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = PickupRequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.household = household
            
            # Logic to auto-assign collector based on Route/Range and Day
            if household.house_no is None:
                messages.error(request, "Please update your profile with your House Number to enable auto-assignment.")
                # Save anyway as pending? Or stop? Let's save as Pending unassigned.
            else:
                # Find Route matching RA and House Range
                routes = tbl_Route.objects.filter(residents_association=household.residents_association)
                target_route = None
                
                print(f"DEBUG: Household RA: {household.residents_association} (ID: {household.residents_association_id}), House No: {household.house_no}")
                print(f"DEBUG: Found {routes.count()} routes for RA.")

                for r in routes:
                    print(f"DEBUG: Checking Route {r.name} (ID: {r.Route_id}): Range {r.start_house_no}-{r.end_house_no}")
                    # Check if house_no falls within range (inclusive)
                    if r.start_house_no is not None and r.end_house_no is not None:
                        if r.start_house_no <= household.house_no <= r.end_house_no:
                            target_route = r
                            print(f"DEBUG: Match found! Route: {r.name}")
                            break
                    else:
                        print("DEBUG: Route has no range defined.")
                
                if target_route:
                     # Find Assignment for the scheduled day
                     day_name = req.scheduled_date.strftime('%A')
                     print(f"DEBUG: Scheduled Day: {day_name}")
                     
                     assignment = tbl_CollectorAssignment.objects.filter(Route_id=target_route, day_of_week=day_name).first()
                     print(f"DEBUG: Assignment Query Result: {assignment}")
                     
                     if assignment:
                         req.assigned_collector = assignment.collector
                         req.status = 'Approved' # Auto-approve if route matches? Or keep pending? User said "Assign Collector", so assigning is key.
                         messages.success(request, f"Pickup request submitted successfully! Assigned to {assignment.collector.collector_name}.")
                     else:
                         messages.warning(request, f"Request submitted. No collector is explicitly assigned to your route ({target_route.name}) on {day_name}. Status is Pending.")
                else:
                    print("DEBUG: No matching route found for house number.")
                    messages.warning(request, "Request submitted. Your house is not currently mapped to a specific pickup route. Admin will review.")
            
            req.save()
            return redirect('view_requests')
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


