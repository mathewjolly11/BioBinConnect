from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth import logout
from GuestApp.models import Collector
from GuestApp.forms import CollectorEditForm, ProfileEditForm

@login_required(login_url='login')
@never_cache
def collector_dashboard(request):
    return render(request, 'Collector/index.html')

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
    from MyApp.models import tbl_PickupRequest, tbl_CollectionRequest
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
            collection.status = 'Completed'
            
            # Initialize other fields to 0 as per plan
            collection.farmer_supply_kg = 0
            collection.leftover_compost_kg = 0
            
            collection.save()
            
            # Update Pickup Request status AND actual weight
            pickup_request.status = 'Completed'
            pickup_request.actual_weight_kg = collection.total_quantity_kg  # Save actual weight
            pickup_request.save()
            
            messages.success(request, f"Collection logged successfully! Collected {collection.total_quantity_kg} kg.")
            return redirect('view_assigned_pickups')
    else:
        form = CollectionLogForm()
    
    return render(request, 'Collector/log_collection.html', {
        'form': form, 
        'pickup': pickup_request
    })


@login_required(login_url='login')
@never_cache
def collection_history(request):
    from MyApp.models import tbl_CollectionRequest
    collector = Collector.objects.get(user=request.user)
    
    history = tbl_CollectionRequest.objects.filter(collector=collector).order_by('-collection_date')
    return render(request, 'Collector/collection_history.html', {'history': history})
