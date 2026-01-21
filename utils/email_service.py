# Email Service Utility for BioBinConnect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags


def send_email(subject, template_name, context, recipient_email):
    """
    Send HTML email using Django's email backend
    
    Args:
        subject: Email subject line
        template_name: Path to HTML template (e.g., 'emails/household/account_approved.html')
        context: Dictionary of context variables for template
        recipient_email: Recipient's email address
    
    Returns:
        Boolean indicating success
    """
    try:
        # Validate email address
        if not recipient_email or '@' not in recipient_email:
            print(f"❌ Invalid recipient email: {recipient_email}")
            return False
            
        # Render HTML content
        html_content = render_to_string(template_name, context)
        text_content = strip_tags(html_content)
        
        # Create email
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[recipient_email]
        )
        email.attach_alternative(html_content, "text/html")
        
        # Send email
        email.send()
        
        # Log success based on backend type
        if settings.EMAIL_BACKEND == 'django.core.mail.backends.console.EmailBackend':
            print(f"✅ Email logged to console: {subject} -> {recipient_email}")
        else:
            print(f"✅ Email sent successfully: {subject} -> {recipient_email}")
            
        return True
        
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Error sending email to {recipient_email}: {e}")
        print(f"   Subject: {subject}")
        print(f"   Template: {template_name}")
        print(f"   Backend: {settings.EMAIL_BACKEND}")
        
        # Handle specific Gmail errors
        if "Daily user sending limit exceeded" in error_msg:
            print("   ⚠️ Gmail daily sending limit reached. Email will retry later.")
        elif "Daily sending quota exceeded" in error_msg:
            print("   ⚠️ Gmail daily quota exceeded. Consider using a different email service.")
        elif "Authentication failed" in error_msg or "Username and Password not accepted" in error_msg:
            print("   ⚠️ Gmail authentication failed. Check EMAIL_HOST_USER and EMAIL_HOST_PASSWORD.")
        elif "Application-specific password required" in error_msg:
            print("   ⚠️ Please use Gmail App Password instead of regular password.")
        
        return False


# ==================== ACCOUNT STATUS EMAILS ====================

def send_account_approved_email(user):
    """Send account approval email to user"""
    role_names = {
        'household': 'Household',
        'collector': 'Collector',
        'farmer': 'Farmer',
        'compost_manager': 'Compost Manager'
    }
    
    context = {
        'user_name': user.name,
        'role': role_names.get(user.role, user.role),
        'login_url': f"{settings.SITE_URL}/login/"
    }
    
    template = f'emails/{user.role}/account_approved.html'
    subject = f'Welcome to BioBinConnect - Account Approved!'
    
    return send_email(subject, template, context, user.email)


def send_account_rejected_email(user, reason=""):
    """Send account rejection email to user"""
    context = {
        'user_name': user.name,
        'reason': reason or 'Your application did not meet our requirements.',
        'contact_email': settings.DEFAULT_FROM_EMAIL
    }
    
    template = f'emails/{user.role}/account_rejected.html'
    subject = 'BioBinConnect - Account Application Status'
    
    return send_email(subject, template, context, user.email)


# ==================== HOUSEHOLD EMAILS ====================

def send_pickup_confirmation_email(pickup_request):
    """Send pickup request confirmation to household"""
    context = {
        'household_name': pickup_request.household.household_name,
        'pickup_id': pickup_request.Pickup_id,
        'scheduled_date': pickup_request.scheduled_date,
        'bin_type': pickup_request.bin_type.name if pickup_request.bin_type else 'N/A',
        'amount_paid': pickup_request.payment_amount,
        'payment_method': pickup_request.payment_method
    }
    
    subject = f'Pickup Request Confirmed - #{pickup_request.Pickup_id}'
    template = 'emails/household/pickup_confirmed.html'
    
    return send_email(subject, template, context, pickup_request.household.user.email)


def send_pickup_scheduled_email(pickup_request):
    """Send pickup scheduled notification with collector details"""
    context = {
        'household_name': pickup_request.household.household_name,
        'pickup_id': pickup_request.Pickup_id,
        'scheduled_date': pickup_request.scheduled_date,
        'collector_name': pickup_request.assigned_collector.collector_name,
        'collector_phone': pickup_request.assigned_collector.user.phone
    }
    
    subject = f'Collector Assigned - Pickup #{pickup_request.Pickup_id}'
    template = 'emails/household/pickup_scheduled.html'
    
    return send_email(subject, template, context, pickup_request.household.user.email)


def send_collection_completed_email(collection_request, pickup_request):
    """Send collection completion receipt to household"""
    context = {
        'household_name': collection_request.household.household_name,
        'collection_date': collection_request.collection_date,
        'weight_collected': collection_request.total_quantity_kg,
        'collector_name': collection_request.collector.collector_name,
        'pickup_id': pickup_request.Pickup_id
    }
    
    subject = f'Collection Completed - #{pickup_request.Pickup_id}'
    template = 'emails/household/collection_completed.html'
    
    return send_email(subject, template, context, collection_request.household.user.email)


# ==================== COLLECTOR EMAILS ====================

def send_route_assignment_email(assignment):
    """Send route assignment notification to collector"""
    context = {
        'collector_name': assignment.collector.collector_name,
        'route_name': assignment.Route_id.name,
        'day_of_week': assignment.day_of_week,
        'location': assignment.Route_id.location.Ward_Name,
        'house_range': f"{assignment.Route_id.start_house_no}-{assignment.Route_id.end_house_no}" if assignment.Route_id.start_house_no else 'N/A'
    }
    
    subject = f'New Route Assigned - {assignment.Route_id.name}'
    template = 'emails/collector/route_assigned.html'
    
    return send_email(subject, template, context, assignment.collector.user.email)


def send_pickup_assignment_email(pickup_request):
    """Send new pickup assignment to collector"""
    context = {
        'collector_name': pickup_request.assigned_collector.collector_name,
        'pickup_id': pickup_request.Pickup_id,
        'household_name': pickup_request.household.household_name,
        'household_address': pickup_request.household.address,
        'house_no': pickup_request.household.house_no,
        'scheduled_date': pickup_request.scheduled_date,
        'bin_type': pickup_request.bin_type.name if pickup_request.bin_type else 'N/A'
    }
    
    subject = f'New Pickup Assigned - #{pickup_request.Pickup_id}'
    template = 'emails/collector/pickup_assigned.html'
    
    return send_email(subject, template, context, pickup_request.assigned_collector.user.email)


# ==================== FARMER EMAILS ====================

def send_order_confirmation_email(order):
    """Send order confirmation to farmer"""
    context = {
        'farmer_name': order.Buyer_id.farmer_name,
        'order_id': order.Order_id,
        'order_date': order.Order_Date,
        'total_amount': order.Total_Amount,
        'delivery_address': order.Delivery_Address
    }
    
    subject = f'Order Confirmed - #{order.Order_id}'
    template = 'emails/farmer/order_confirmed.html'
    
    return send_email(subject, template, context, order.Buyer_id.user.email)


# ==================== ADMIN EMAILS ====================

def send_new_registration_alert(user):
    """Send new registration alert to admin"""
    from GuestApp.models import CustomUser
    
    # Get admin users
    admin_users = CustomUser.objects.filter(is_superuser=True)
    
    role_names = {
        'household': 'Household',
        'collector': 'Collector',
        'farmer': 'Farmer',
        'compost_manager': 'Compost Manager'
    }
    
    context = {
        'user_name': user.name,
        'user_email': user.email,
        'user_phone': user.phone,
        'role': role_names.get(user.role, user.role),
        'admin_url': f"{settings.SITE_URL}/view_users/"
    }
    
    subject = f'New {role_names.get(user.role, user.role)} Registration - Action Required'
    template = 'emails/admin/new_registration.html'
    
    # Send to all admins
    for admin in admin_users:
        send_email(subject, template, context, admin.email)
    
    return True


def send_registration_confirmation_email(user, password):
    """Send registration confirmation with login credentials to user"""
    role_names = {
        'household': 'Household',
        'collector': 'Collector',
        'farmer': 'Farmer',
        'compost_manager': 'Compost Manager'
    }
    
    context = {
        'user_name': user.name,
        'user_email': user.email,
        'password': password,
        'role': role_names.get(user.role, user.role),
        'login_url': f"{settings.SITE_URL}/login/"
    }
    
    subject = 'Registration Successful - BioBinConnect'
    template = 'emails/household/registration_success.html'
    
    return send_email(subject, template, context, user.email)
