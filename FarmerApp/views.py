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
