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
