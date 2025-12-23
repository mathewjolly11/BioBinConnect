from django.shortcuts import redirect, render
from django.contrib import messages

from MyApp.forms import DistrictForm,LocationForm,RAForm
from MyApp.models import tbl_residentsassociation

# Create your views here.
def index(request):
    return render(request, 'Admin/index.html')
def add_district(request):
    if request.method == 'POST':
        form = DistrictForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'District added successfully!')
            return redirect('view_districts')
    else:
        form = DistrictForm()
    return render(request, 'Admin/add_district.html', {'form': form})

def view_districts(request):
    from MyApp.models import tbl_District
    districts = tbl_District.objects.all()
    return render(request, 'Admin/view_districts.html' , {'districts': districts}) 

def edit_district(request, district_id):
    from MyApp.models import tbl_District
    district= tbl_District.objects.get(District_id=district_id)
    if request.method == 'POST':
        form=DistrictForm(request.POST, instance=district)
        if form.is_valid():
            form.save()
            messages.success(request, 'District updated successfully!')
            return redirect('view_districts')
    else:
        form=DistrictForm(instance=district)
    return render(request, 'Admin/add_district.html', {'form': form})

def delete_district(request, district_id):
    from MyApp.models import tbl_District
    district = tbl_District.objects.get(District_id=district_id)
    district.delete()
    messages.success(request, 'District deleted successfully!')
    return redirect('view_districts')

def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Location added successfully!')
            return redirect('view_districts')
    else:
        form = LocationForm()
    return render(request, 'Admin/add_location.html', {'form': form})

def view_locations(request):
    from MyApp.models import tbl_location
    locations = tbl_location.objects.all()
    return render(request, 'Admin/view_locations.html' , {'locations': locations})

def edit_location(request, location_id):
    from MyApp.models import tbl_location
    location= tbl_location.objects.get(Location_id=location_id)
    if request.method == 'POST':
        form=LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            messages.success(request, 'Location updated successfully!')
            return redirect('view_locations')
    else:
        form=LocationForm(instance=location)
    return render(request, 'Admin/add_location.html', {'form': form})

def delete_location(request, location_id):
    from MyApp.models import tbl_location
    location = tbl_location.objects.get(Location_id=location_id)
    location.delete()
    messages.success(request, 'Location deleted successfully!')
    return redirect('view_locations')   

def add_ra(request):
    from MyApp.forms import RAForm
    if request.method == 'POST':
        form = RAForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Residents Association added successfully!')
            return redirect('view_ra')
    else:
        form = RAForm()
    return render(request, 'Admin/add_ra.html', {'form': form})

def view_ra(request):
    ra_list = tbl_residentsassociation.objects.all()
    return render(request, 'Admin/view_ra.html' , {'ra_list': ra_list})

def edit_ra(request, ra_id):
    ra= tbl_residentsassociation.objects.get(RA_id=ra_id)
    if request.method == 'POST':
        form=RAForm(request.POST, instance=ra)
        if form.is_valid():
            form.save()
            messages.success(request, 'Residents Association updated successfully!')
            return redirect('view_ra')
    else:
        form=RAForm(instance=ra)
    return render(request, 'Admin/add_ra.html', {'form': form})

def delete_ra(request, ra_id):
    from MyApp.models import tbl_residentsassociation
    ra = tbl_residentsassociation.objects.get(RA_id=ra_id)
    ra.delete()
    messages.success(request, 'Residents Association deleted successfully!')
    return redirect('view_ra')

def view_users(request):
    """View all users for admin verification"""
    from GuestApp.models import CustomUser, Household, Collector, CompostManager, Farmer
    
    users = CustomUser.objects.exclude(is_superuser=True).select_related().order_by('-date_joined')
    
    # Get role-specific details for each user
    user_data = []
    for user in users:
        data = {
            'user': user,
            'role_details': None
        }
        
        if user.role == 'household':
            try:
                data['role_details'] = Household.objects.get(user=user)
            except Household.DoesNotExist:
                pass
        elif user.role == 'collector':
            try:
                data['role_details'] = Collector.objects.get(user=user)
            except Collector.DoesNotExist:
                pass
        elif user.role == 'compost_manager':
            try:
                data['role_details'] = CompostManager.objects.get(user=user)
            except CompostManager.DoesNotExist:
                pass
        elif user.role == 'farmer':
            try:
                data['role_details'] = Farmer.objects.get(user=user)
            except Farmer.DoesNotExist:
                pass
        
        user_data.append(data)
    
    return render(request, 'Admin/view_users.html', {'user_data': user_data})

def approve_user(request, user_id):
    """Approve/verify a user"""
    from GuestApp.models import CustomUser
    
    user = CustomUser.objects.get(id=user_id)
    user.is_verified = True
    user.save()
    messages.success(request, f'User {user.name} has been approved successfully!')
    return redirect('view_users')

def reject_user(request, user_id):
    """Reject/unverify a user"""
    from GuestApp.models import CustomUser
    
    user = CustomUser.objects.get(id=user_id)
    user.is_verified = False
    user.save()
    messages.warning(request, f'User {user.name} has been rejected!')
    return redirect('view_users')
