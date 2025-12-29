from django.shortcuts import redirect, render
from django.contrib import messages
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta

from MyApp.forms import DistrictForm,LocationForm,RAForm
from MyApp.models import tbl_residentsassociation

# Create your views here.
def index(request):
    """Enhanced admin dashboard with real-time statistics"""
    from MyApp.models import (
        tbl_Order, tbl_PaymentTransaction, tbl_WasteInventory, 
        tbl_CompostBatch, tbl_HouseholdPayment
    )
    from GuestApp.models import Collector, CompostManager, Farmer, Household
    
    # User Statistics
    total_collectors = Collector.objects.count()
    total_managers = CompostManager.objects.count()
    total_farmers = Farmer.objects.count()
    total_households = Household.objects.count()
    total_users = total_collectors + total_managers + total_farmers + total_households
    
    # Pending verifications - count users with is_verified=False
    pending_collectors = Collector.objects.filter(user__is_verified=False).count()
    pending_managers = CompostManager.objects.filter(user__is_verified=False).count()
    pending_farmers = Farmer.objects.filter(user__is_verified=False).count()
    pending_households = Household.objects.filter(user__is_verified=False).count()
    pending_verifications = pending_collectors + pending_managers + pending_farmers + pending_households
    
    # Revenue Statistics (Last 30 days)
    thirty_days_ago = timezone.now() - timedelta(days=30)
    
    # Orders revenue
    recent_orders = tbl_Order.objects.filter(Order_Date__gte=thirty_days_ago)
    total_revenue = recent_orders.aggregate(total=Sum('Total_Amount'))['total'] or 0
    total_orders = recent_orders.count()
    
    # Payment transactions
    successful_payments = tbl_PaymentTransaction.objects.filter(
        status='Success',
        transaction_date__gte=thirty_days_ago
    )
    payment_revenue = successful_payments.aggregate(total=Sum('Amount'))['total'] or 0
    
    # Household payments
    household_payments = tbl_HouseholdPayment.objects.filter(
        payment_date__gte=thirty_days_ago,
        status='Completed'
    )
    household_revenue = household_payments.aggregate(total=Sum('amount'))['total'] or 0
    
    # Inventory Statistics
    waste_stock = tbl_WasteInventory.objects.filter(is_available=True).aggregate(
        total=Sum('available_quantity_kg')
    )['total'] or 0
    
    compost_stock = tbl_CompostBatch.objects.filter(Status='Available').aggregate(
        total=Sum('Stock_kg')
    )['total'] or 0
    
    # Today's statistics
    today = timezone.now().date()
    today_orders = tbl_Order.objects.filter(Order_Date__date=today).count()
    today_revenue = tbl_Order.objects.filter(Order_Date__date=today).aggregate(
        total=Sum('Total_Amount')
    )['total'] or 0
    
    # Recent activities (last 5 orders)
    recent_activities = tbl_Order.objects.select_related('Buyer_id').order_by('-Order_Date')[:5]
    
    context = {
        # User stats
        'total_users': total_users,
        'total_collectors': total_collectors,
        'total_managers': total_managers,
        'total_farmers': total_farmers,
        'pending_verifications': pending_verifications,
        
        # Revenue stats
        'total_revenue': total_revenue,
        'total_orders': total_orders,
        'payment_revenue': payment_revenue,
        'household_revenue': household_revenue,
        
        # Inventory stats
        'waste_stock': waste_stock,
        'compost_stock': compost_stock,
        
        # Today's stats
        'today_orders': today_orders,
        'today_revenue': today_revenue,
        
        # Recent activities
        'recent_activities': recent_activities,
    }
    
    return render(request, 'Admin/index.html', context)
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

def assign_collector(request):
    from MyApp.forms import CollectorAssignmentForm
    from MyApp.models import tbl_CollectorAssignment
    
    if request.method == 'POST':
        form = CollectorAssignmentForm(request.POST)
        
        # Custom validation for assign_all_week
        assign_all_week = request.POST.get('assign_all_week') == 'on'
        if not assign_all_week and not request.POST.get('day_of_week'):
            form.add_error('day_of_week', 'This field is required when not assigning for all week.')
        
        if form.is_valid():
            collector = form.cleaned_data['collector']
            route = form.cleaned_data['Route_id']
            
            if assign_all_week:
                # Assign collector for all days of the week
                days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                created_count = 0
                existing_count = 0
                
                for day in days:
                    # Check if assignment already exists for this collector, route, and day
                    assignment, created = tbl_CollectorAssignment.objects.get_or_create(
                        collector=collector,
                        Route_id=route,
                        day_of_week=day
                    )
                    if created:
                        created_count += 1
                    else:
                        existing_count += 1
                
                if created_count > 0 and existing_count > 0:
                    messages.success(request, f'Collector assigned for {created_count} new days. {existing_count} assignments already existed.')
                elif created_count > 0:
                    messages.success(request, f'Collector assigned successfully for all {created_count} days of the week!')
                else:
                    messages.info(request, 'Collector was already assigned for all days of the week on this route.')
            else:
                # Single day assignment
                day_of_week = form.cleaned_data['day_of_week']
                assignment, created = tbl_CollectorAssignment.objects.get_or_create(
                    collector=collector,
                    Route_id=route,
                    day_of_week=day_of_week
                )
                if created:
                    messages.success(request, f'Collector assigned successfully for {day_of_week}!')
                else:
                    messages.info(request, f'Collector was already assigned for {day_of_week} on this route.')
            
            return redirect('view_assignments')
    else:
        form = CollectorAssignmentForm()
    
    return render(request, 'Admin/assign_collector.html', {'form': form})

def view_assignments(request):
    from MyApp.models import tbl_CollectorAssignment
    from django.db.models import Q
    from collections import defaultdict
    
    assignments = tbl_CollectorAssignment.objects.select_related('collector', 'Route_id').all().order_by('collector__collector_name', 'Route_id__name', 'day_of_week')
    
    # Group assignments by collector and route for better display
    grouped_assignments = defaultdict(lambda: defaultdict(list))
    for assignment in assignments:
        key = (assignment.collector.collector_name, assignment.Route_id.name)
        grouped_assignments[assignment.collector.collector_name][assignment.Route_id.name].append(assignment.day_of_week)
    
    return render(request, 'Admin/view_assignments.html', {
        'assignments': assignments,
        'grouped_assignments': dict(grouped_assignments)
    })

def add_route(request):
    from MyApp.forms import RouteForm
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Route added successfully!')
            return redirect('view_routes')
    else:
        form = RouteForm()
    return render(request, 'Admin/add_route.html', {'form': form})

def view_routes(request):
    from MyApp.models import tbl_Route
    routes = tbl_Route.objects.select_related('location').all()
    return render(request, 'Admin/view_routes.html', {'routes': routes})

def payment_report(request):
    """View payment reports with summary and filters"""
    from MyApp.models import tbl_HouseholdPayment
    from django.db.models import Sum
    from datetime import date
    
    # Base queryset
    payments = tbl_HouseholdPayment.objects.select_related('household', 'bin_type').order_by('-payment_date')
    
    # Filters
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    status = request.GET.get('status')
    
    if from_date:
        payments = payments.filter(payment_date__date__gte=from_date)
    if to_date:
        payments = payments.filter(payment_date__date__lte=to_date)
    if status:
        payments = payments.filter(status=status)
        
    # Calculate filtered totals
    filtered_total = payments.aggregate(Sum('amount'))['amount__sum'] or 0
    
    # Daily statistics (for cards)
    today = date.today()
    all_payments = tbl_HouseholdPayment.objects.all()
    today_payments = all_payments.filter(payment_date__date=today)
    
    today_total = today_payments.aggregate(Sum('amount'))['amount__sum'] or 0
    today_count = today_payments.count()
    today_completed = today_payments.filter(status='Completed').count()
    
    all_total = all_payments.aggregate(Sum('amount'))['amount__sum'] or 0
    all_count = all_payments.count()
    
    context = {
        'payments': payments,
        'today_total': today_total,
        'today_count': today_count,
        'today_completed': today_completed,
        'all_total': all_total,
        'all_count': all_count,
        'filtered_total': filtered_total,
        'from_date': from_date or '',
        'to_date': to_date or '',
        'status': status or '',
        'check_completed': status == 'Completed',
        'check_pending': status == 'Pending',
    }
    
    return render(request, 'Admin/payment_report_v3.html', context)

def export_payment_report(request):
    """Export payment report to CSV"""
    import csv
    from django.http import HttpResponse
    from MyApp.models import tbl_HouseholdPayment
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="payment_report.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Date', 'Household', 'House No', 'Bin Type', 'Amount', 'Transaction ID', 'Status'])
    
    # Re-apply filters
    payments = tbl_HouseholdPayment.objects.select_related('household', 'bin_type').order_by('-payment_date')
    
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    status = request.GET.get('status')
    
    if from_date:
        payments = payments.filter(payment_date__date__gte=from_date)
    if to_date:
        payments = payments.filter(payment_date__date__lte=to_date)
    if status:
        payments = payments.filter(status=status)
    
    for payment in payments:
        writer.writerow([
            payment.Payment_id,
            payment.payment_date.strftime('%Y-%m-%d %H:%M') if payment.payment_date else '',
            payment.household.household_name if payment.household else 'N/A',
            payment.household.house_no if payment.household else 'N/A',
            payment.bin_type.name if payment.bin_type else 'N/A',
            payment.amount,
            payment.transaction_id,
            payment.status
        ])
        
    return response

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from MyApp.models import tbl_Order, tbl_OrderItem, tbl_FarmerSupply, tbl_PaymentTransaction
from django.db.models import Sum, Count, Q
from decimal import Decimal


@login_required(login_url='login')
@never_cache
def admin_waste_sales(request):
    """Admin view for waste sales tracking"""
    
    # Get all waste orders
    waste_orders = tbl_Order.objects.filter(
        tbl_orderitem__Item_Type='Waste'
    ).distinct().select_related('Buyer_id').prefetch_related('tbl_orderitem_set').order_by('-Order_Date')
    
    # Apply filters
    status_filter = request.GET.get('status', 'all')
    if status_filter != 'all':
        waste_orders = waste_orders.filter(Payment_Status=status_filter)
    
    # Calculate statistics
    total_orders = waste_orders.count()
    total_revenue = waste_orders.aggregate(total=Sum('Total_Amount'))['total'] or Decimal('0.00')
    pending_orders = waste_orders.filter(Payment_Status='Pending').count()
    completed_orders = waste_orders.filter(Payment_Status='Paid').count()
    
    context = {
        'orders': waste_orders,
        'status_filter': status_filter,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'pending_orders': pending_orders,
        'completed_orders': completed_orders,
    }
    return render(request, 'Admin/waste_sales.html', context)


@login_required(login_url='login')
@never_cache
def admin_compost_sales(request):
    """Admin view for compost sales tracking"""
    
    # Get all compost orders
    compost_orders = tbl_Order.objects.filter(
        tbl_orderitem__Item_Type='Compost'
    ).distinct().select_related('Buyer_id').prefetch_related('tbl_orderitem_set').order_by('-Order_Date')
    
    # Apply filters
    status_filter = request.GET.get('status', 'all')
    if status_filter != 'all':
        compost_orders = compost_orders.filter(Payment_Status=status_filter)
    
    # Calculate statistics
    total_orders = compost_orders.count()
    total_revenue = compost_orders.aggregate(total=Sum('Total_Amount'))['total'] or Decimal('0.00')
    pending_orders = compost_orders.filter(Payment_Status='Pending').count()
    completed_orders = compost_orders.filter(Payment_Status='Paid').count()
    
    context = {
        'orders': compost_orders,
        'status_filter': status_filter,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'pending_orders': pending_orders,
        'completed_orders': completed_orders,
    }
    return render(request, 'Admin/compost_sales.html', context)


@login_required(login_url='login')
@never_cache
def admin_update_delivery_status(request, order_id):
    """Update delivery status for an order"""
    if request.method == 'POST':
        try:
            order = tbl_Order.objects.get(Order_id=order_id)
            new_status = request.POST.get('delivery_status')
            
            # Update all order items
            order.tbl_orderitem_set.all().update(Delivery_Status=new_status)
            
            messages.success(request, f'Delivery status updated to {new_status}')
        except Exception as e:
            messages.error(request, f'Error updating status: {str(e)}')
    
    # Redirect back to appropriate page
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)

def admin_profile(request):
    """View for admin profile page"""
    context = {
        'user': request.user,
    }
    return render(request, 'Admin/admin_profile.html', context)

def view_aadhaar(request, user_id):
    """View to display user's Aadhaar image"""
    from GuestApp.models import CustomUser, Household, Farmer
    from django.http import Http404
    
    try:
        user = CustomUser.objects.get(id=user_id)
        aadhaar_image = None
        user_type = None
        
        if user.role == 'household':
            try:
                household = Household.objects.get(user=user)
                aadhaar_image = household.aadhaar_image
                user_type = 'Household'
            except Household.DoesNotExist:
                pass
        elif user.role == 'farmer':
            try:
                farmer = Farmer.objects.get(user=user)
                aadhaar_image = farmer.aadhaar_image
                user_type = 'Farmer'
            except Farmer.DoesNotExist:
                pass
        
        if not aadhaar_image:
            raise Http404("Aadhaar image not found for this user")
        
        context = {
            'user': user,
            'aadhaar_image': aadhaar_image,
            'user_type': user_type,
        }
        return render(request, 'Admin/view_aadhaar.html', context)
        
    except CustomUser.DoesNotExist:
        raise Http404("User not found")

def add_bin_type(request):
    """Add a new bin type"""
    from MyApp.forms import BinTypeForm
    if request.method == 'POST':
        form = BinTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bin type added successfully!')
            return redirect('view_bin_types')
    else:
        form = BinTypeForm()
    return render(request, 'Admin/add_bin_type.html', {'form': form})

def view_bin_types(request):
    """View all bin types"""
    from MyApp.models import tbl_BinType
    bin_types = tbl_BinType.objects.all().order_by('capacity_kg')
    return render(request, 'Admin/view_bin_types.html', {'bin_types': bin_types})

def edit_bin_type(request, bin_type_id):
    """Edit an existing bin type"""
    from MyApp.models import tbl_BinType
    from MyApp.forms import BinTypeForm
    bin_type = tbl_BinType.objects.get(BinType_id=bin_type_id)
    if request.method == 'POST':
        form = BinTypeForm(request.POST, instance=bin_type)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bin type updated successfully!')
            return redirect('view_bin_types')
    else:
        form = BinTypeForm(instance=bin_type)
    return render(request, 'Admin/add_bin_type.html', {'form': form})

def delete_bin_type(request, bin_type_id):
    """Delete a bin type"""
    from MyApp.models import tbl_BinType
    bin_type = tbl_BinType.objects.get(BinType_id=bin_type_id)
    bin_type.delete()
    messages.success(request, 'Bin type deleted successfully!')
    return redirect('view_bin_types')
