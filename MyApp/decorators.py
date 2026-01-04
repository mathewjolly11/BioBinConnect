"""
Custom decorators for BioBinConnect authentication and authorization
"""
from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps


def admin_required(view_func):
    """
    Decorator to restrict access to admin users only.
    Checks if user is logged in and is a superuser (admin).
    Shows custom error pages for unauthorized access.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        from django.shortcuts import render
        
        # Check if user is authenticated
        if not request.user.is_authenticated:
            # Show custom 401 error page for non-authenticated users
            return render(request, 'errors/401.html', status=401)
        
        # Check if user is admin (superuser)
        if not request.user.is_superuser:
            # Render custom 403 error page for authenticated non-admins
            return render(request, 'errors/403.html', status=403)
        
        # User is authenticated and is admin
        return view_func(request, *args, **kwargs)
    
    return wrapper


def role_required(*allowed_roles):
    """
    Decorator to restrict access to specific user roles.
    Usage: @role_required('admin', 'collector', 'farmer')
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # Check if user is authenticated
            if not request.user.is_authenticated:
                messages.warning(request, 'Please login to continue.')
                return redirect('login')
            
            # Check if user has admin privilege (bypass role check for admins)
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            
            # Check if user's role is in allowed roles
            if hasattr(request.user, 'role') and request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            
            messages.error(request, 'You do not have permission to access this page.')
            return redirect('home')
        
        return wrapper
    return decorator
