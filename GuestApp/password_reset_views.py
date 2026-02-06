import threading
import logging
import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
import random
from django.template.loader import render_to_string
from .models import CustomUser, PasswordResetOTP

# Configure logging
logging.basicConfig(
    filename='email_debug.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, plain_message, recipient_list, from_email):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.plain_message = plain_message
        self.from_email = from_email
        threading.Thread.__init__(self)

    def run(self):
        try:
            logging.info(f"🚀 Starting email thread to: {self.recipient_list}")
            logging.info(f"📧 From: {self.from_email}")
            
            email_msg = EmailMultiAlternatives(
                self.subject,
                self.plain_message,
                self.from_email,
                self.recipient_list
            )
            email_msg.attach_alternative(self.html_content, "text/html")
            email_msg.send(fail_silently=False)
            
            logging.info(f"✅ Email sent successfully to {self.recipient_list}")
            print(f"✅ Email sent successfully to {self.recipient_list}")
            
        except Exception as e:
            logging.error(f"❌ Error sending email: {str(e)}")
            import traceback
            logging.error(traceback.format_exc())
            print(f"❌ Error sending email: {str(e)}")

def get_sender_email():
    """Helper to ensure we use the authenticated email address"""
    if settings.EMAIL_HOST_USER:
        return f"BioBinConnect <{settings.EMAIL_HOST_USER}>"
    return settings.DEFAULT_FROM_EMAIL

def forgot_password_request(request):
    """Handle forgot password request - send OTP to email"""
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        
        # Check if user exists
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            messages.error(request, 'No account found with this email address.')
            return render(request, 'Guest/forgot_password.html')
        
        # Generate 6-digit OTP
        otp_code = str(random.randint(100000, 999999))
        
        # Set expiry time (5 minutes from now)
        expires_at = timezone.now() + timedelta(minutes=5)
        
        # Delete any existing OTPs for this user
        PasswordResetOTP.objects.filter(user=user).delete()
        
        # Create new OTP
        PasswordResetOTP.objects.create(
            user=user,
            otp_code=otp_code,
            expires_at=expires_at
        )
        
from django.http import JsonResponse

def forgot_password_request(request):
    """Handle forgot password request - send OTP to email"""
    if request.method == 'POST':
        # specific handling for AJAX requests (if needed) or checking headers
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        email = request.POST.get('email', '').strip()
        
        # Check if user exists
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            if is_ajax:
                return JsonResponse({'success': False, 'message': 'No account found with this email address.'})
            messages.error(request, 'No account found with this email address.')
            return render(request, 'Guest/forgot_password.html')
        
        # Generate 6-digit OTP
        otp_code = str(random.randint(100000, 999999))
        
        # Set expiry time (5 minutes from now)
        expires_at = timezone.now() + timedelta(minutes=5)
        
        # Delete any existing OTPs for this user
        PasswordResetOTP.objects.filter(user=user).delete()
        
        # Create new OTP
        PasswordResetOTP.objects.create(
            user=user,
            otp_code=otp_code,
            expires_at=expires_at
        )
        
        # Send OTP via email using HTML template
        subject = 'BioBinConnect - Password Reset OTP'
        
        # Render HTML email template
        html_message = render_to_string('emails/password_reset_otp.html', {
            'user_name': user.name,
            'otp_code': otp_code,
        })
        
        # Plain text fallback
        plain_message = f"""
Hello {user.name},

You requested to reset your password for BioBinConnect.

Your OTP code is: {otp_code}

This code will expire in 5 minutes.

If you didn't request this, please ignore this email.

Best regards,
BioBinConnect Team
        """
        
        # Get valid sender
        from_email = get_sender_email()
        
        # Send OTP Synchronously (Blocking) so user only sees next page if successful
        try:
            email_msg = EmailMultiAlternatives(
                subject,
                plain_message,
                from_email,
                [email]
            )
            email_msg.attach_alternative(html_message, "text/html")
            email_msg.send(fail_silently=False)
            print(f"✅ OTP Email sent successfully to {email}")
            
            # Store email in session for next step
            request.session['reset_email'] = email
            
            if is_ajax:
                return JsonResponse({'success': True, 'message': 'OTP sent successfully', 'redirect_url': '/verify-otp/'})
                
            messages.success(request, f'OTP has been sent to {email}. Please check your inbox.')
            return redirect('verify_otp')
            
        except Exception as e:
            print(f"❌ Error sending OTP email: {str(e)}")
            if is_ajax:
                return JsonResponse({'success': False, 'message': f"Error sending email: {str(e)}"})
            messages.error(request, f"Error sending email: {str(e)}")
            return render(request, 'Guest/forgot_password.html')
            
    return render(request, 'Guest/forgot_password.html')


def verify_otp(request):
    """Verify OTP code"""
    email = request.session.get('reset_email')
    
    if not email:
        messages.error(request, 'Session expired. Please start again.')
        return redirect('forgot_password_request')
    
    if request.method == 'POST':
        otp_code = request.POST.get('otp_code', '').strip()
        
        try:
            user = CustomUser.objects.get(email=email)
            otp = PasswordResetOTP.objects.filter(
                user=user,
                otp_code=otp_code
            ).first()
            
            if not otp:
                messages.error(request, 'Invalid OTP code.')
                return render(request, 'Guest/verify_otp.html', {'email': email})
            
            if not otp.is_valid():
                messages.error(request, 'OTP has expired or already been used. Please request a new one.')
                return render(request, 'Guest/verify_otp.html', {'email': email})
            
            # OTP is valid - mark as used and proceed to reset password
            otp.is_used = True
            otp.save()
            
            request.session['otp_verified'] = True
            messages.success(request, 'OTP verified successfully. Please set your new password.')
            return redirect('reset_password')
            
        except CustomUser.DoesNotExist:
            messages.error(request, 'User not found.')
            return redirect('forgot_password_request')
    
    return render(request, 'Guest/verify_otp.html', {'email': email})


def resend_otp(request):
    """Resend OTP to email"""
    email = request.session.get('reset_email')
    
    if not email:
        messages.error(request, 'Session expired. Please start again.')
        return redirect('forgot_password_request')
    
    try:
        user = CustomUser.objects.get(email=email)
        
        # Generate new OTP
        otp_code = str(random.randint(100000, 999999))
        expires_at = timezone.now() + timedelta(minutes=5)
        
        # Delete old OTPs
        PasswordResetOTP.objects.filter(user=user).delete()
        
        # Create new OTP
        PasswordResetOTP.objects.create(
            user=user,
            otp_code=otp_code,
            expires_at=expires_at
        )
        
        # Send email
        subject = 'BioBinConnect - Password Reset OTP (Resent)'
        html_message = render_to_string('emails/password_reset_otp.html', {
            'user_name': user.name,
            'otp_code': otp_code,
        })
        plain_message = f"Hello {user.name}, Your new OTP code is: {otp_code}."
        
        # Get valid sender
        from_email = get_sender_email()
        
        # Send Synchronously
        email_msg = EmailMultiAlternatives(
            subject,
            plain_message,
            from_email,
            [email]
        )
        email_msg.attach_alternative(html_message, "text/html")
        email_msg.send(fail_silently=False)
        
        messages.success(request, 'New OTP has been sent to your email.')
        
    except Exception as e:
        messages.error(request, f'Error resending OTP: {str(e)}')
    
    return redirect('verify_otp')


def reset_password(request):
    """Reset password after OTP verification"""
    email = request.session.get('reset_email')
    otp_verified = request.session.get('otp_verified', False)
    
    if not email or not otp_verified:
        messages.error(request, 'Please verify OTP first.')
        return redirect('forgot_password_request')
    
    if request.method == 'POST':
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        new_password = request.POST.get('new_password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()
        
        # Validate passwords
        if not new_password or not confirm_password:
            msg = 'Please fill in all fields.'
            if is_ajax: return JsonResponse({'success': False, 'message': msg})
            messages.error(request, msg)
            return render(request, 'Guest/reset_password.html')
        
        if new_password != confirm_password:
            msg = 'Passwords do not match.'
            if is_ajax: return JsonResponse({'success': False, 'message': msg})
            messages.error(request, msg)
            return render(request, 'Guest/reset_password.html')
        
        if len(new_password) < 6:
            msg = 'Password must be at least 6 characters long.'
            if is_ajax: return JsonResponse({'success': False, 'message': msg})
            messages.error(request, msg)
            return render(request, 'Guest/reset_password.html')
        
        try:
            user = CustomUser.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            
            # Clear session data
            request.session.pop('reset_email', None)
            request.session.pop('otp_verified', None)
            
            # Delete used OTPs
            PasswordResetOTP.objects.filter(user=user).delete()
            
            # Send confirmation email
            subject = 'BioBinConnect - Password Reset Successful'
            html_message = render_to_string('emails/password_reset_success.html', {
                'user_name': user.name,
                'login_url': f"{settings.SITE_URL}/login/",
            })
            plain_message = f"Hello {user.name},\n\nYour password has been successfully reset."
            
            # Get valid sender
            from_email = get_sender_email()
            
            # Send in background (keep async for success email to not block login)
            EmailThread(subject, html_message, plain_message, [email], from_email).start()
            
            if is_ajax:
                return JsonResponse({'success': True, 'message': 'Password reset successful! Redirecting to login...', 'redirect_url': '/login/'})

            messages.success(request, 'Password reset successful! Please login with your new password.')
            return redirect('login')
            
        except CustomUser.DoesNotExist:
            msg = 'User not found.'
            if is_ajax: return JsonResponse({'success': False, 'message': msg})
            messages.error(request, msg)
            return redirect('forgot_password_request')
    
    return render(request, 'Guest/reset_password.html')
