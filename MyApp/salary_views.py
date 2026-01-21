from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.db.models import Count
from django.http import JsonResponse
from decimal import Decimal
import json

from GuestApp.models import Collector, CompostManager
from MyApp.models import tbl_WasteInventory, tbl_CompostBatch, tbl_PaymentTransaction


@login_required(login_url='login')
@never_cache
def admin_salary_management(request):
    """Admin page to manage salary payments for collectors and managers"""
    
    # Get all active collectors with their unpaid collection dates
    collectors = Collector.objects.filter(user__is_verified=True)
    collector_data = []
    
    for collector in collectors:
        # Get unpaid collection dates (unique dates, not individual records)
        unpaid_dates = tbl_WasteInventory.objects.filter(
            collector=collector,
            salary_paid=False
        ).values('collection_date__date').annotate(
            collections_count=Count('Inventory_id')
        ).order_by('collection_date__date')
        
        total_unpaid_days = unpaid_dates.count()
        
        # Convert dates to serializable format
        # Convert dates to serializable format (Force evaluation and string conversion)
        unpaid_dates_list = [
            {
                'collection_date__date': str(item['collection_date__date']),
                'collections_count': item['collections_count']
            }
            for item in unpaid_dates
        ]
        
        collector_data.append({
            'collector': collector,
            'unpaid_days': total_unpaid_days,
            'total_due': total_unpaid_days * 1000,  # ₹1000/day
            'unpaid_dates_json': json.dumps(unpaid_dates_list, default=str)  # JSON string for JavaScript
        })
    
    # Get all active compost managers with their unpaid batch creation dates
    managers = CompostManager.objects.filter(user__is_verified=True)
    manager_data = []
    
    for manager in managers:
        # Get unpaid batch creation dates (unique dates)
        unpaid_dates = tbl_CompostBatch.objects.filter(
            CompostManager_id=manager,
            salary_paid=False
        ).values('Date_Created').annotate(
            batches_count=Count('Batch_id')
        ).order_by('Date_Created')
        
        total_unpaid_days = unpaid_dates.count()
        
        # Convert dates to serializable format
        # Convert dates to serializable format (Force evaluation and string conversion)
        unpaid_dates_list = [
            {
                'Date_Created': str(item['Date_Created']),
                'batches_count': item['batches_count']
            }
            for item in unpaid_dates
        ]
        
        manager_data.append({
            'manager': manager,
            'unpaid_days': total_unpaid_days,
            'total_due': total_unpaid_days * 1000,  # ₹1000/day
            'unpaid_dates_json': json.dumps(unpaid_dates_list, default=str)  # JSON string for JavaScript
        })
    
    context = {
        'collectors': collector_data,
        'managers': manager_data,
        'daily_rate': 1000,
        'has_unpaid_collectors': any(item['unpaid_days'] > 0 for item in collector_data),
        'has_unpaid_managers': any(item['unpaid_days'] > 0 for item in manager_data),
    }
    
    return render(request, 'Admin/salary_management.html', context)


@login_required(login_url='login')
@never_cache
def admin_pay_salary(request):
    """Process salary payment for selected dates"""
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'pay_all_collectors':
            # Pay all collectors with unpaid days
            try:
                total_amount = 0
                count = 0
                
                for collector in collectors:
                    unpaid_dates = tbl_WasteInventory.objects.filter(
                        collector=collector,
                        salary_paid=False
                    ).values('collection_date__date').distinct()
                    
                    if unpaid_dates.exists():
                        # Mark all unpaid collections as paid
                        tbl_WasteInventory.objects.filter(
                            collector=collector,
                            salary_paid=False
                        ).update(salary_paid=True)
                        
                        # Calculate amount
                        days_count = unpaid_dates.count()
                        amount = days_count * 1000
                        total_amount += amount
                        count += 1
                        
                        # Create payment transaction
                        tbl_PaymentTransaction.objects.create(
                            Payer_id=request.user,
                            Receiver_id=collector.user,
                            Amount=amount,
                            transaction_type='CollectorSalary',
                            Reference_id=None,
                            status='Success'
                        )
                
                messages.success(request, f'Paid salaries to {count} collectors. Total amount: ₹{total_amount:,.2f}')
                return redirect('admin_salary_management')
                
            except Exception as e:
                messages.error(request, f'Error paying collectors: {str(e)}')
                return redirect('admin_salary_management')
        
        elif action == 'pay_all_managers':
            # Pay all managers with unpaid days
            try:
                total_amount = 0
                count = 0
                
                for manager in managers:
                    unpaid_dates = tbl_CompostBatch.objects.filter(
                        CompostManager_id=manager,
                        salary_paid=False
                    ).values('Date_Created').distinct()
                    
                    if unpaid_dates.exists():
                        # Mark all unpaid batches as paid
                        tbl_CompostBatch.objects.filter(
                            CompostManager_id=manager,
                            salary_paid=False
                        ).update(salary_paid=True)
                        
                        # Calculate amount
                        days_count = unpaid_dates.count()
                        amount = days_count * 1000
                        total_amount += amount
                        count += 1
                        
                        # Create payment transaction
                        tbl_PaymentTransaction.objects.create(
                            Payer_id=request.user,
                            Receiver_id=manager.user,
                            Amount=amount,
                            transaction_type='ManagerSalary',
                            Reference_id=None,
                            status='Success'
                        )
                
                messages.success(request, f'Paid salaries to {count} managers. Total amount: ₹{total_amount:,.2f}')
                return redirect('admin_salary_management')
                
            except Exception as e:
                messages.error(request, f'Error paying managers: {str(e)}')
                return redirect('admin_salary_management')
        
        # Original single payment logic
        try:
            user_type = request.POST.get('user_type')  # 'collector' or 'manager'
            user_id = request.POST.get('user_id')
            selected_dates = request.POST.getlist('selected_dates[]')  # List of dates as strings
            
            if not selected_dates:
                return JsonResponse({'success': False, 'error': 'No dates selected'})
            
            # Calculate total amount
            total_days = len(selected_dates)
            total_amount = total_days * 1000  # ₹1000/day
            
            if user_type == 'collector':
                collector = Collector.objects.get(pk=user_id)
                receiver_user = collector.user
                
                # Mark collections as paid for selected dates
                for date_str in selected_dates:
                    tbl_WasteInventory.objects.filter(
                        collector=collector,
                        collection_date__date=date_str,
                        salary_paid=False
                    ).update(salary_paid=True)
                
                transaction_type = 'CollectorSalary'
                name = collector.collector_name
                reference_note = f'{name} salary for {total_days} days'
                
            elif user_type == 'manager':
                manager = CompostManager.objects.get(pk=user_id)
                receiver_user = manager.user
                
                # Mark batches as paid for selected dates
                for date_str in selected_dates:
                    tbl_CompostBatch.objects.filter(
                        CompostManager_id=manager,
                        Date_Created=date_str,
                        salary_paid=False
                    ).update(salary_paid=True)
                
                transaction_type = 'ManagerSalary'
                name = manager.compostmanager_name
                reference_note = f'{name} salary for {total_days} days'
            else:
                return JsonResponse({'success': False, 'error': 'Invalid user type'})
            
            # Create payment transaction
            transaction = tbl_PaymentTransaction.objects.create(
                Payer_id=request.user,  # Admin user
                Receiver_id=receiver_user,
                Amount=total_amount,
                transaction_type=transaction_type,
                Reference_id=None,  # No specific order reference
                status='Success'
            )
            
            success_msg = f'Salary of ₹{total_amount:,.2f} paid to {name} for {total_days} days'
            # messages.success(request, success_msg)  <-- Removed to prevent duplicate alert
            return JsonResponse({
                'success': True,
                'message': success_msg,
                'transaction_id': transaction.Transaction_id
            })
            
        except Exception as e:
            # messages.error(request, f'Error processing payment: {str(e)}') <-- Removed
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@login_required(login_url='login')
@never_cache
def manager_salaries(request):
    """Manager Salaries - Shows actual payments made via Salary Management"""
    from django.utils import timezone
    from datetime import timedelta
    
    # Get filter parameters
    period_filter = request.GET.get('period', '30')
    
    # Date filtering
    start_date = None
    if period_filter != 'all':
        days = int(period_filter)
        start_date = timezone.now() - timedelta(days=days)
    
    # Get actual salary payments from transactions
    salary_payments = tbl_PaymentTransaction.objects.filter(
        status='Success',
        transaction_type='ManagerSalary'
    ).select_related('Receiver_id')
    
    if start_date:
        salary_payments = salary_payments.filter(transaction_date__gte=start_date)
    
    # Group payments by manager
    from django.db.models import Sum, Count
    manager_payment_summary = salary_payments.values(
        'Receiver_id',
        'Receiver_id__name',
        'Receiver_id__email'
    ).annotate(
        total_paid=Sum('Amount'),
        payment_count=Count('Transaction_id')
    ).order_by('-total_paid')
    
    # Get all managers for complete view
    all_managers = CompostManager.objects.filter(user__is_verified=True).select_related('user')
    
    # Build manager data with payment info
    manager_salaries_data = []
    total_salary_paid = 0
    
    for manager in all_managers:
        # Find payment summary for this manager
        paid_amount = 0
        payment_count = 0
        
        for summary in manager_payment_summary:
            if summary['Receiver_id'] == manager.user.id:
                paid_amount = summary['total_paid'] or 0
                payment_count = summary['payment_count'] or 0
                break
        
        total_salary_paid += paid_amount
        
        manager_salaries_data.append({
            'manager': manager,
            'name': manager.compostmanager_name if hasattr(manager, 'compostmanager_name') else manager.user.username,
            'email': manager.user.email if hasattr(manager.user, 'email') else 'N/A',
            'total_paid': paid_amount,
            'payment_count': payment_count,
            'has_payments': paid_amount > 0
        })
    
    # Sort by total paid (descending)
    manager_salaries_data.sort(key=lambda x: x['total_paid'], reverse=True)
    
    context = {
        'manager_salaries': manager_salaries_data,
        'total_salary_paid': total_salary_paid,
        'total_managers': len(manager_salaries_data),
        'managers_with_payments': sum(1 for m in manager_salaries_data if m['has_payments']),
        'daily_salary': 1000,  # Reference rate
        'period_filter': period_filter,
    }
    
    return render(request, 'Admin/manager_salaries.html', context)


@login_required(login_url='login')
@never_cache
def pay_salary_confirm(request, user_type, user_id):
    """Render a dedicated page for salary confirmation"""
    daily_rate = 1000
    
    if user_type == 'collector':
        collector = Collector.objects.get(pk=user_id)
        name = collector.collector_name
        email = collector.user.email
        
        # Get unpaid dates
        unpaid_dates = tbl_WasteInventory.objects.filter(
            collector=collector,
            salary_paid=False
        ).values('collection_date__date').annotate(
            work_count=Count('Inventory_id')
        ).order_by('collection_date__date')
        
    elif user_type == 'manager':
        manager = CompostManager.objects.get(pk=user_id)
        name = manager.compostmanager_name
        email = manager.user.email
        
        unpaid_dates = tbl_CompostBatch.objects.filter(
            CompostManager_id=manager,
            salary_paid=False
        ).values('Date_Created').annotate(
            work_count=Count('Batch_id')
        ).order_by('Date_Created')
        
    else:
        messages.error(request, 'Invalid user type')
        return redirect('admin_salary_management')

    # Format dates for template
    dates_data = []
    for item in unpaid_dates:
        date_val = item.get('collection_date__date') or item.get('Date_Created')
        dates_data.append({
            'date': str(date_val),
            'count': item['work_count']
        })

    context = {
        'user_type': user_type,
        'user_id': user_id,
        'name': name,
        'email': email,
        'dates': dates_data,
        'daily_rate': daily_rate,
        'total_unpaid_days': len(dates_data),
        'total_amount': len(dates_data) * daily_rate
    }
    
    return render(request, 'Admin/pay_salary_confirm.html', context)
