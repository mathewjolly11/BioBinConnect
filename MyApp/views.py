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

def assign_collector(request):
    from MyApp.forms import CollectorAssignmentForm
    if request.method == 'POST':
        form = CollectorAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Collector assigned successfully!')
            return redirect('view_assignments')
    else:
        form = CollectorAssignmentForm()
    return render(request, 'Admin/assign_collector.html', {'form': form})

def view_assignments(request):
    from MyApp.models import tbl_CollectorAssignment
    assignments = tbl_CollectorAssignment.objects.select_related('collector', 'Route_id').all()
    return render(request, 'Admin/view_assignments.html', {'assignments': assignments})

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
