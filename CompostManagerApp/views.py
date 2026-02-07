from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth import logout
from django.db.models import Sum, Q
from django.utils import timezone
from GuestApp.models import CompostManager
from GuestApp.forms import CompostManagerEditForm, ProfileEditForm
from MyApp.models import tbl_WasteInventory, tbl_CompostBatch
from .forms import CreateCompostBatchForm, CompostBatchForm, BatchStatusUpdateForm
from decimal import Decimal

@login_required(login_url='login')
@never_cache
def compost_manager_dashboard(request):
    """Enhanced dashboard with statistics"""
    compost_manager = CompostManager.objects.get(user=request.user)
    
    # Get statistics
    total_available_waste = tbl_WasteInventory.objects.filter(
        status='Available'
    ).aggregate(total=Sum('available_quantity_kg'))['total'] or 0
    
    active_batches = tbl_CompostBatch.objects.filter(
        CompostManager_id=compost_manager,
        Status__in=['Processing', 'Ready']
    ).count()
    
    ready_stock = tbl_CompostBatch.objects.filter(
        CompostManager_id=compost_manager,
        Status='Ready'
    ).aggregate(total=Sum('Stock_kg'))['total'] or 0
    
    recent_batches = tbl_CompostBatch.objects.filter(
        CompostManager_id=compost_manager
    ).order_by('-Date_Created')[:5]
    
    context = {
        'compost_manager': compost_manager,
        'total_available_waste': total_available_waste,
        'active_batches': active_batches,
        'ready_stock': ready_stock,
        'recent_batches': recent_batches,
    }
    return render(request, 'CompostManager/index.html', context)

@login_required(login_url='login')
@never_cache
def view_waste_inventory(request):
    """View all available waste from collectors"""
    # Get all waste inventory
    all_waste = tbl_WasteInventory.objects.all().select_related('collector', 'collection_request').order_by('-collection_date')
    
    # Filter by availability if requested
    status_filter = request.GET.get('status', 'all')
    if status_filter == 'available':
        all_waste = all_waste.filter(status='Available')
    elif status_filter == 'used':
        all_waste = all_waste.filter(status='Used')
    
    context = {
        'waste_inventory': all_waste,
        'status_filter': status_filter,
    }
    return render(request, 'CompostManager/waste_inventory.html', context)

@login_required(login_url='login')
@never_cache
def create_compost_batch(request):
    """Create new compost batch from available waste"""
    compost_manager = CompostManager.objects.get(user=request.user)
    
    # Get available waste
    available_waste = tbl_WasteInventory.objects.filter(
        status='Available',
        available_quantity_kg__gt=0
    ).select_related('collector')
    
    if request.method == 'POST':
        form = CreateCompostBatchForm(request.POST)
        waste_ids = request.POST.getlist('waste_ids')
        
        if form.is_valid() and waste_ids:
            # Calculate total waste from selected items
            selected_waste = tbl_WasteInventory.objects.filter(Inventory_id__in=waste_ids)
            total_waste = selected_waste.aggregate(total=Sum('available_quantity_kg'))['total'] or 0
            
            # Get conversion ratio from settings (with fallback to 4.0)
            from MyApp.models import SystemSettings
            conversion_ratio = Decimal(SystemSettings.get_setting('compost_conversion_ratio', '4.0'))
            
            # Conversion ratio: X kg waste = 1 kg compost
            compost_stock = total_waste / conversion_ratio
            
            # Create compost batch
            batch = form.save(commit=False)
            batch.CompostManager_id = compost_manager
            batch.Date_Created = timezone.now().date()
            batch.Status = 'Processing'
            batch.Grade = 'A'  # All compost is standard quality
            batch.Source_Waste_kg = total_waste  # Auto-set from selected waste
            batch.Stock_kg = compost_stock  # Calculated based on conversion ratio
            batch.price_per_kg = Decimal('200.00')  # Fixed price: ₹200 per 1kg packet
            
            batch.save()
            
            # Update waste inventory - mark as used
            selected_waste.update(status='Used')
            
            messages.success(request, f'Compost batch "{batch.Batch_name}" created successfully!')
            return redirect('manage_batches')
        else:
            if not waste_ids:
                messages.error(request, 'Please select at least one waste item.')
            else:
                messages.error(request, 'Please correct the errors below.')
    else:
        form = CreateCompostBatchForm()
    
    # Get conversion ratio from settings for display in template
    from MyApp.models import SystemSettings
    conversion_ratio = SystemSettings.get_setting('compost_conversion_ratio', '4.0')
    
    context = {
        'form': form,
        'available_waste': available_waste,
        'conversion_ratio': conversion_ratio,
    }
    return render(request, 'CompostManager/create_batch.html', context)

@login_required(login_url='login')
@never_cache
def manage_batches(request):
    """List and manage all compost batches"""
    compost_manager = CompostManager.objects.get(user=request.user)
    
    # Get all batches for this manager
    batches = tbl_CompostBatch.objects.filter(
        CompostManager_id=compost_manager
    ).order_by('-Date_Created')
    
    # Filter by status if requested
    status_filter = request.GET.get('status', 'all')
    if status_filter != 'all':
        batches = batches.filter(Status=status_filter)
    
    context = {
        'batches': batches,
        'status_filter': status_filter,
    }
    return render(request, 'CompostManager/manage_batches.html', context)

@login_required(login_url='login')
@never_cache
def update_batch_status(request, batch_id):
    """Update batch status"""
    compost_manager = CompostManager.objects.get(user=request.user)
    batch = get_object_or_404(tbl_CompostBatch, Batch_id=batch_id, CompostManager_id=compost_manager)
    
    if request.method == 'POST':
        form = BatchStatusUpdateForm(request.POST)
        if form.is_valid():
            new_status = form.cleaned_data['status']
            batch.Status = new_status
            batch.save()
            messages.success(request, f'Batch status updated to "{new_status}"')
            return redirect('manage_batches')
    
    return redirect('manage_batches')

@login_required(login_url='login')
@never_cache
def edit_batch(request, batch_id):
    """Edit batch details"""
    print(f"DEBUG: Entering edit_batch with batch_id={batch_id}, user={request.user}")
    try:
        compost_manager = CompostManager.objects.get(user=request.user)
        print(f"DEBUG: Found manager: {compost_manager}")
        batch = get_object_or_404(tbl_CompostBatch, Batch_id=batch_id, CompostManager_id=compost_manager)
        print(f"DEBUG: Found batch: {batch}")
        
        if request.method == 'POST':
            print("DEBUG: Processing POST request")
            form = CompostBatchForm(request.POST, instance=batch)
            if form.is_valid():
                form.save()
                messages.success(request, 'Batch updated successfully!')
                return redirect('manage_batches')
            else:
                print(f"DEBUG: Form invalid: {form.errors}")
                messages.error(request, 'Please correct the errors below.')
        else:
            print("DEBUG: Processing GET request")
            form = CompostBatchForm(instance=batch)
            print(f"DEBUG: Form initialized with fields: {list(form.fields.keys())}")
        
        context = {
            'form': form,
            'batch': batch,
            'is_edit': True,
        }
        return render(request, 'CompostManager/edit_batch.html', context)
    except Exception as e:
        print(f"DEBUG: Exception in edit_batch: {e}")
        import traceback
        traceback.print_exc()
        messages.error(request, f"Error loading batch: {str(e)}")
        return redirect('manage_batches')


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

@login_required(login_url='login')
@never_cache
def delete_account(request):
    """Delete compost manager account permanently"""
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()  # This will cascade delete the compost manager profile
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('login')
    
    return render(request, 'CompostManager/delete_account_confirm.html')

def services(request):
    """Display services page for compost managers"""
    manager = CompostManager.objects.get(user=request.user)
    return render(request, 'CompostManager/services.html', {'manager': manager})

def contact(request):
    """Display contact page for compost managers"""
    manager = CompostManager.objects.get(user=request.user)
    return render(request, 'CompostManager/contact.html', {'manager': manager})

def about_us(request):
    """Display about page for compost managers"""
    manager = CompostManager.objects.get(user=request.user)
    return render(request, 'CompostManager/about.html', {'manager': manager})
