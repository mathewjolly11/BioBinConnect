from django.shortcuts import redirect, render
from django.contrib import messages
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta, datetime
from MyApp.decorators import admin_required

from MyApp.forms import DistrictForm,LocationForm,RAForm
from MyApp.models import tbl_residentsassociation

# Helper function for system alerts
def get_system_alerts():
    """Check for system alerts based on configured thresholds"""
    from MyApp.models import SystemSettings, tbl_CompostBatch, tbl_WasteInventory
    from GuestApp.models import CustomUser
    
    alerts = []
    
    # Get settings
    low_stock_threshold = int(SystemSettings.get_setting('low_stock_threshold', '50'))
    expiry_warning_days = int(SystemSettings.get_setting('expiry_warning_days', '7'))
    
    # Check compost stock
    total_compost_stock = tbl_CompostBatch.objects.filter(
        Status__in=['Processing', 'Ready']
    ).aggregate(total=Sum('Stock_kg'))['total'] or 0
    
    if total_compost_stock < low_stock_threshold:
        alerts.append({
            'type': 'danger',
            'icon': 'fa-exclamation-triangle',
            'title': 'Low Compost Stock',
            'message': f'Only {int(total_compost_stock)} packets available (threshold: {low_stock_threshold} packets)',
            'priority': 1
        })
    
    # Check waste stock
    total_waste_stock = tbl_WasteInventory.objects.filter(
        status='Available'
    ).aggregate(total=Sum('available_quantity_kg'))['total'] or 0
    
    if total_waste_stock < low_stock_threshold:
        alerts.append({
            'type': 'warning',
            'icon': 'fa-recycle',
            'title': 'Low Waste Stock',
            'message': f'Only {total_waste_stock}kg waste available (threshold: {low_stock_threshold}kg)',
            'priority': 2
        })
    
    # Check pending user approvals (exclude admins)
    pending_users = CustomUser.objects.filter(is_verified=False, is_active=True).exclude(role='admin').count()
    if pending_users > 0:
        alerts.append({
            'type': 'warning',
            'icon': 'fa-user-plus',
            'title': 'Pending User Verifications',
            'message': f'{pending_users} user(s) waiting for approval',
            'priority': 2
        })
    
    # Sort by priority
    alerts.sort(key=lambda x: x['priority'])
    
    return alerts

def get_recent_activities():
    """Fetch and normalize recent system activities"""
    from GuestApp.models import CustomUser
    from MyApp.models import (
        tbl_PickupRequest, tbl_Order, 
        tbl_HouseholdPayment, tbl_CompostBatch
    )
    activities = []
    
    # 1. New User Registrations
    users = CustomUser.objects.order_by('-date_joined')[:5]
    for u in users:
        activities.append({
            'type': 'User',
            'icon': 'fa-user-plus',
            'color': 'primary',
            'time': u.date_joined,
            'description': f"New user registered: {u.name} ({u.role})"
        })
        
    # 2. Pickup Requests
    pickups = tbl_PickupRequest.objects.order_by('-scheduled_date')[:5]
    for p in pickups:
        # Convert date to datetime for sorting compatibility
        dt = datetime.combine(p.scheduled_date, datetime.min.time())
        activities.append({
            'type': 'Pickup',
            'icon': 'fa-truck',
            'color': 'info',
            'time': timezone.make_aware(dt) if timezone.is_naive(dt) else dt,
            'description': f"Pickup requested by {p.household.household_name}"
        })

    # 3. Orders
    orders = tbl_Order.objects.order_by('-Order_Date')[:5]
    for o in orders:
        activities.append({
            'type': 'Order',
            'icon': 'fa-shopping-cart',
            'color': 'success',
            'time': o.Order_Date,
            'description': f"New order #{o.Order_id} from {o.Buyer_id.farmer_name} (₹{o.Total_Amount})"
        })
        
    # 4. Payments
    payments = tbl_HouseholdPayment.objects.order_by('-payment_date')[:5]
    for pay in payments:
        activities.append({
            'type': 'Payment',
            'icon': 'fa-credit-card',
            'color': 'warning',
            'time': pay.payment_date,
            'description': f"Payment received from {pay.household.household_name} (₹{pay.amount})"
        })
        
    # 5. Compost Batches (using Date_Created)
    batches = tbl_CompostBatch.objects.order_by('-Date_Created')[:5]
    for b in batches:
        dt = datetime.combine(b.Date_Created, datetime.min.time())
        activities.append({
            'type': 'Batch',
            'icon': 'fa-flask',
            'color': 'purple', # Will use custom css or mapped class
            'time': timezone.make_aware(dt) if timezone.is_naive(dt) else dt,
            'description': f"New compost batch created: {b.Batch_name}"
        })
    
    # Sort by time desc
    activities.sort(key=lambda x: x['time'], reverse=True)
    return activities[:10]


@admin_required
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
    waste_stock = tbl_WasteInventory.objects.filter(
        status='Available'
    ).aggregate(
        total=Sum('available_quantity_kg')
    )['total'] or 0
    
    compost_stock = tbl_CompostBatch.objects.filter(Status='Ready').aggregate(
        total=Sum('Stock_kg')
    )['total'] or 0
    
    # Today's statistics
    today = timezone.now().date()
    today_orders = tbl_Order.objects.filter(Order_Date__date=today).count()
    today_revenue = tbl_Order.objects.filter(Order_Date__date=today).aggregate(
        total=Sum('Total_Amount')
    )['total'] or 0
    
    # Recent activities (timeline)
    recent_activities = get_recent_activities()
    
    # Get system alerts
    system_alerts = get_system_alerts()
    
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
        
        # System alerts
        'system_alerts': system_alerts,
    }
    
    return render(request, 'Admin/index.html', context)
@admin_required
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

@admin_required
def view_districts(request):
    from MyApp.models import tbl_District
    districts = tbl_District.objects.all()
    return render(request, 'Admin/view_districts.html' , {'districts': districts}) 

@admin_required
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

@admin_required
def delete_district(request, district_id):
    from MyApp.models import tbl_District
    district = tbl_District.objects.get(District_id=district_id)
    district.delete()
    messages.success(request, 'District deleted successfully!')
    return redirect('view_districts')

@admin_required
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

@admin_required
def view_locations(request):
    from MyApp.models import tbl_location
    locations = tbl_location.objects.all()
    return render(request, 'Admin/view_locations.html' , {'locations': locations})

@admin_required
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

@admin_required
def delete_location(request, location_id):
    from MyApp.models import tbl_location
    location = tbl_location.objects.get(Location_id=location_id)
    location.delete()
    messages.success(request, 'Location deleted successfully!')
    return redirect('view_locations')   

@admin_required
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

@admin_required
def view_ra(request):
    ra_list = tbl_residentsassociation.objects.all()
    return render(request, 'Admin/view_ra.html' , {'ra_list': ra_list})

@admin_required
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

@admin_required
def delete_ra(request, ra_id):
    from MyApp.models import tbl_residentsassociation
    ra = tbl_residentsassociation.objects.get(RA_id=ra_id)
    ra.delete()
    messages.success(request, 'Residents Association deleted successfully!')
    return redirect('view_ra')

@admin_required
def view_users(request):
    """View all users for admin verification"""
    from GuestApp.models import CustomUser, Household, Collector, CompostManager, Farmer
    
    users = CustomUser.objects.exclude(is_superuser=True).select_related().order_by('-date_joined')
    
    # Handle Export
    if request.GET.get('export') == 'excel':
        from MyApp.utils import generate_excel_report
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="User_List_{timezone.now().strftime("%Y-%m-%d")}.xlsx"'
        
        headers = ["Name", "Role", "Email", "Date Joined", "Status", "Verified"]
        data = []
        
        for user in users:
            data.append([
                user.name,
                user.role.capitalize(),
                user.email,
                user.date_joined.strftime('%Y-%m-%d %H:%M'),
                user.account_status,
                "Yes" if user.is_verified else "No"
            ])
            
        generate_excel_report(response, "User List Report", headers, data)
        return response
    
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

@admin_required
def approve_user(request, user_id):
    """Approve/verify a user"""
    from GuestApp.models import CustomUser
    
    user = CustomUser.objects.get(id=user_id)
    user.is_verified = True
    user.account_status = 'Approved'
    user.save()
    
    # Send approval email to user
    try:
        from utils.email_service import send_account_approved_email
        send_account_approved_email(user)
    except Exception as e:
        print(f"Email notification failed: {e}")
    
    messages.success(request, f'User {user.name} has been approved successfully!')
    return redirect('view_users')

@admin_required
def reject_user(request, user_id):
    """Reject/unverify a user"""
    from GuestApp.models import CustomUser
    
    user = CustomUser.objects.get(id=user_id)
    user.is_verified = False
    user.account_status = 'Rejected'
    user.save()
    
    # Send rejection email to user
    try:
        from utils.email_service import send_account_rejected_email
        send_account_rejected_email(user, reason="Your application did not meet our verification requirements.")
    except Exception as e:
        print(f"Email notification failed: {e}")
    
    messages.warning(request, f'User {user.name} has been rejected!')
    return redirect('view_users')

@admin_required
def approve_all_users(request):
    """Approve all pending users"""
    from GuestApp.models import CustomUser
    
    # Bulk update for efficiency
    updated_count = CustomUser.objects.filter(account_status='Pending').exclude(role='admin').update(is_verified=True, account_status='Approved')
    
    if updated_count > 0:
        messages.success(request, f'Successfully approved {updated_count} pending users!')
    else:
        messages.info(request, 'No pending users found to approve.')
        
    return redirect('view_users')

@admin_required
def reject_all_users(request):
    """Reject all pending users"""
    from GuestApp.models import CustomUser
    
    # Bulk update for efficiency
    updated_count = CustomUser.objects.filter(account_status='Pending').exclude(role='admin').update(is_verified=False, account_status='Rejected')
    
    if updated_count > 0:
        messages.warning(request, f'Rejected {updated_count} pending users.')
    else:
        messages.info(request, 'No pending users found to reject.')
        
    return redirect('view_users')

@admin_required
def assign_collector(request):
    from MyApp.forms import CollectorAssignmentForm
    from MyApp.models import tbl_CollectorAssignment
    import json
    
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
                        # Send route assignment email for each new assignment
                        try:
                            from utils.email_service import send_route_assignment_email
                            send_route_assignment_email(assignment)
                        except Exception as e:
                            print(f"Email notification failed: {e}")
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
    
    # Get all existing assignments grouped by route and day
    # Structure: {route_id: {day: collector_name}}
    assignments = tbl_CollectorAssignment.objects.select_related('collector', 'Route_id').all()
    assignments_data = {}
    
    for assignment in assignments:
        route_id = assignment.Route_id.Route_id
        day = assignment.day_of_week
        collector_name = assignment.collector.collector_name
        
        if route_id not in assignments_data:
            assignments_data[route_id] = {}
        assignments_data[route_id][day] = collector_name
    
    # Convert to JSON for JavaScript
    assignments_json = json.dumps(assignments_data)
    
    return render(request, 'Admin/assign_collector.html', {
        'form': form,
        'assignments_json': assignments_json
    })

@admin_required
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

@admin_required
def delete_assignment(request, assignment_id):
    """Delete a collector assignment"""
    from django.http import JsonResponse
    from MyApp.models import tbl_CollectorAssignment
    
    if request.method == 'POST':
        try:
            assignment = tbl_CollectorAssignment.objects.get(Assign_id=assignment_id)
            collector_name = assignment.collector.collector_name
            route_name = assignment.Route_id.name
            day = assignment.day_of_week
            
            assignment.delete()
            
            messages.success(request, f'Assignment deleted successfully: {collector_name} - {route_name} ({day})')
            
            return JsonResponse({
                'success': True,
                'message': 'Assignment deleted successfully'
            })
            
        except tbl_CollectorAssignment.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': 'Assignment not found'
            }, status=404)
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'error': 'Invalid request method'
    }, status=405)

@admin_required
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

@admin_required
def view_routes(request):
    from MyApp.models import tbl_Route
    routes = tbl_Route.objects.select_related('location').all()
    return render(request, 'Admin/view_routes.html', {'routes': routes})

@admin_required
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
        'check_failed': status == 'Failed',
    }
    
    return render(request, 'Admin/payment_report_v3.html', context)

@admin_required
def export_payment_report(request):
    """Export payment report to Excel"""
    from MyApp.utils import generate_excel_report
    from django.http import HttpResponse
    from django.utils import timezone
    from MyApp.models import tbl_HouseholdPayment
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="Household_Payments_{timezone.now().strftime("%Y-%m-%d")}.xlsx"'
    
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
        
    headers = ['ID', 'Date', 'Household', 'House No', 'Bin Type', 'Amount', 'Transaction ID', 'Status']
    data = []
    
    for payment in payments:
        data.append([
            payment.Payment_id,
            payment.payment_date.strftime('%Y-%m-%d %H:%M'),
            payment.household.household_name,
            payment.household.house_no,
            payment.bin_type.name,
            payment.amount,
            payment.transaction_id,
            payment.status
        ])
    
    generate_excel_report(response, "Household Payments Report", headers, data)
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

@admin_required
def admin_profile(request):
    """View for admin profile page"""
    if request.method == 'POST':
        # Handle password change
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        # Validate current password
        if not request.user.check_password(current_password):
            messages.error(request, 'Current password is incorrect.')
        # Validate new passwords match
        elif new_password != confirm_password:
            messages.error(request, 'New passwords do not match.')
        # Validate password length
        elif len(new_password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
        else:
            # Change password
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, 'Password changed successfully!')
            # Re-authenticate user to maintain session
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(request, request.user)
    
    context = {
        'user': request.user,
    }
    return render(request, 'Admin/admin_profile.html', context)

@admin_required
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

@admin_required
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

@admin_required
def view_bin_types(request):
    """View all bin types"""
    from MyApp.models import tbl_BinType
    bin_types = tbl_BinType.objects.all().order_by('capacity_kg')
    return render(request, 'Admin/view_bin_types.html', {'bin_types': bin_types})

@admin_required
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

@admin_required
def delete_bin_type(request, bin_type_id):
    """Delete a bin type"""
    from MyApp.models import tbl_BinType
    bin_type = tbl_BinType.objects.get(BinType_id=bin_type_id)
    bin_type.delete()
    messages.success(request, 'Bin type deleted successfully!')
    return redirect('view_bin_types')

@admin_required
def edit_user(request, user_id):
    """Edit user information for all roles"""
    from GuestApp.models import CustomUser, Household, Collector, CompostManager, Farmer
    from MyApp.models import tbl_District, tbl_location, tbl_residentsassociation
    
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        messages.error(request, 'User not found!')
        return redirect('view_users')
    
    # Get role-specific details
    role_details = None
    if user.role == 'household':
        try:
            role_details = Household.objects.get(user=user)
        except Household.DoesNotExist:
            pass
    elif user.role == 'collector':
        try:
            role_details = Collector.objects.get(user=user)
        except Collector.DoesNotExist:
            pass
    elif user.role == 'compost_manager':
        try:
            role_details = CompostManager.objects.get(user=user)
        except CompostManager.DoesNotExist:
            pass
    elif user.role == 'farmer':
        try:
            role_details = Farmer.objects.get(user=user)
        except Farmer.DoesNotExist:
            pass
    
    if request.method == 'POST':
        # Update basic user information
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.save()
        
        # Update role-specific information
        if role_details:
            if user.role == 'household':
                role_details.household_name = request.POST.get('household_name')
                role_details.phone = request.POST.get('role_phone')
                role_details.address = request.POST.get('address')
                role_details.house_no = request.POST.get('house_no')
                
                # Update district, location, and RA if changed
                district_id = request.POST.get('district')
                location_id = request.POST.get('location')
                ra_id = request.POST.get('residents_association')
                
                if district_id:
                    role_details.district = tbl_District.objects.get(District_id=district_id)
                if location_id:
                    role_details.location = tbl_location.objects.get(Location_id=location_id)
                if ra_id:
                    role_details.residents_association = tbl_residentsassociation.objects.get(RA_id=ra_id)
                
                role_details.save()
                
            elif user.role == 'collector':
                role_details.collector_name = request.POST.get('collector_name')
                role_details.phone = request.POST.get('role_phone')
                role_details.address = request.POST.get('address')
                role_details.save()
                
            elif user.role == 'compost_manager':
                role_details.compostmanager_name = request.POST.get('compostmanager_name')
                role_details.phone = request.POST.get('role_phone')
                role_details.address = request.POST.get('address')
                role_details.license_number = request.POST.get('license_number')
                role_details.save()
                
            elif user.role == 'farmer':
                role_details.farmer_name = request.POST.get('farmer_name')
                role_details.phone = request.POST.get('role_phone')
                role_details.address = request.POST.get('address')
                role_details.save()
        
        messages.success(request, f'User {user.name} updated successfully!')
        return redirect('view_users')
    
    # Prepare context for template
    context = {
        'user': user,
        'role_details': role_details,
    }
    
    # Add additional data for household users
    if user.role == 'household':
        context['districts'] = tbl_District.objects.all()
        context['locations'] = tbl_location.objects.all()
        context['residents_associations'] = tbl_residentsassociation.objects.all()
    
    return render(request, 'Admin/edit_user.html', context)

def change_user_password(request, user_id):
    """Change user password"""
    from GuestApp.models import CustomUser
    
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        messages.error(request, 'User not found!')
        return redirect('view_users')
    
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        # Validate passwords match
        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'Admin/change_password.html', {'user': user})
        
        # Validate password length
        if len(new_password) < 6:
            messages.error(request, 'Password must be at least 6 characters long!')
            return render(request, 'Admin/change_password.html', {'user': user})
        
        # Set new password using Django's secure method
        user.set_password(new_password)
        user.save()
        
        messages.success(request, f'Password for {user.name} changed successfully!')
        return redirect('view_users')
    
    return render(request, 'Admin/change_password.html', {'user': user})


# Admin system settings
@admin_required
def admin_settings(request):
    """Manage system-wide settings"""
    from MyApp.forms import SystemSettingsForm
    from MyApp.models import SystemSettings
    
    if request.method == 'POST':
        form = SystemSettingsForm(request.POST)
        if form.is_valid():
            # Save compost conversion ratio
            ratio = str(form.cleaned_data['compost_conversion_ratio'])
            SystemSettings.set_setting(
                'compost_conversion_ratio', 
                ratio,
                'Waste to compost conversion ratio (kg waste per 1kg compost)'
            )
            
            # Save inventory alert settings
            low_stock = str(form.cleaned_data['low_stock_threshold'])
            SystemSettings.set_setting(
                'low_stock_threshold',
                low_stock,
                'Low stock warning threshold in kg'
            )
            
            expiry_days = str(form.cleaned_data['expiry_warning_days'])
            SystemSettings.set_setting(
                'expiry_warning_days',
                expiry_days,
                'Days before expiry to show warning'
            )
            
            unavailable_days = str(form.cleaned_data['auto_unavailable_days'])
            SystemSettings.set_setting(
                'auto_unavailable_days',
                unavailable_days,
                'Days after which waste is automatically marked unavailable'
            )
            
            # Save waste price per kg
            waste_price = str(form.cleaned_data['waste_price_per_kg'])
            SystemSettings.set_setting(
                'waste_price_per_kg',
                waste_price,
                'Default price for waste sold to farmers per kilogram (in ₹)'
            )
            
            messages.success(request, 'System settings updated successfully!')
            return redirect('admin_settings')
    else:
        form = SystemSettingsForm()
    
    # Get current settings for display
    current_ratio = SystemSettings.get_setting('compost_conversion_ratio', '4.0')
    current_low_stock = SystemSettings.get_setting('low_stock_threshold', '50')
    current_expiry_days = SystemSettings.get_setting('expiry_warning_days', '7')
    current_unavailable_days = SystemSettings.get_setting('auto_unavailable_days', '30')
    current_waste_price = SystemSettings.get_setting('waste_price_per_kg', '10.00')
    
    context = {
        'form': form,
        'current_ratio': current_ratio,
        'current_low_stock': current_low_stock,
        'current_expiry_days': current_expiry_days,
        'current_unavailable_days': current_unavailable_days,
        'current_waste_price': current_waste_price,
    }
    return render(request, 'Admin/settings.html', context)


def custom_404(request, exception):
    """Custom 404 error page handler"""
    return render(request, 'errors/404.html', status=404)
