from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
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
