from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from GuestApp.models import CompostManager
from GuestApp.forms import CompostManagerEditForm, ProfileEditForm

@login_required(login_url='login')
@never_cache
def compost_manager_dashboard(request):
    return render(request, 'CompostManager/index.html')

@login_required(login_url='login')
@never_cache
def compost_manager_profile(request):
    compost_manager = CompostManager.objects.get(user=request.user)
    context = {
        'compost_manager': compost_manager,
        'user': request.user
    }
    return render(request, 'CompostManager/profile.html', context)

@login_required(login_url='login')
@never_cache
def edit_profile(request):
    """Edit compost manager profile"""
    compost_manager = CompostManager.objects.get(user=request.user)
    
    if request.method == 'POST':
        user_form = ProfileEditForm(request.POST, instance=request.user)
        compost_form = CompostManagerEditForm(request.POST, request.FILES, instance=compost_manager)
        
        if user_form.is_valid() and compost_form.is_valid():
            user_form.save()
            compost_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('compost_manager_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = ProfileEditForm(instance=request.user)
        compost_form = CompostManagerEditForm(instance=compost_manager)
    
    context = {
        'user_form': user_form,
        'compost_form': compost_form,
        'compost_manager': compost_manager,
        'user': request.user
    }
    return render(request, 'CompostManager/edit_profile.html', context)
