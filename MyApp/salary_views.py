from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.utils import timezone
from GuestApp.models import CompostManager
from datetime import timedelta


@login_required(login_url='login')
@never_cache
def manager_salaries(request):
    """Dedicated compost manager salary management page"""
    
    # Get filter parameters
    period_filter = request.GET.get('period', '30')
    
    # Calculate date range
    if period_filter == 'all':
        start_date = None
    else:
        days = int(period_filter)
        start_date = timezone.now() - timedelta(days=days)
    
    # Fixed daily salary
    daily_salary = 1000
    
    # Get all verified compost managers
    compost_managers = CompostManager.objects.filter(
        user__is_verified=True
    ).select_related('user')
    
    # Calculate salaries for each manager
    manager_salaries = []
    total_salary_expense = 0
    
    for manager in compost_managers:
        # Calculate days worked
        join_date = manager.user.date_joined
        
        if start_date:
            # If manager joined after start_date, use join_date
            if join_date < start_date:
                days_worked = (timezone.now().date() - start_date.date()).days + 1
            else:
                days_worked = (timezone.now().date() - join_date.date()).days + 1
        else:
            # All time - from join date to now
            days_worked = (timezone.now().date() - join_date.date()).days + 1
        
        # Ensure at least 1 day
        days_worked = max(1, days_worked)
        
        total_salary = days_worked * daily_salary
        total_salary_expense += total_salary
        
        manager_salaries.append({
            'manager': manager,
            'join_date': join_date,
            'days_worked': days_worked,
            'daily_rate': daily_salary,
            'total_salary': total_salary
        })
    
    # Sort by total salary (highest first)
    manager_salaries.sort(key=lambda x: x['total_salary'], reverse=True)
    
    context = {
        'manager_salaries': manager_salaries,
        'total_salary_expense': total_salary_expense,
        'daily_salary': daily_salary,
        'total_managers': len(manager_salaries),
        'period_filter': period_filter,
    }
    
    return render(request, 'Admin/manager_salaries.html', context)
