import os
import django
from django.conf import settings
from django.core.mail import send_mail
import sys

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')
django.setup()

def test_email():
    print("--- Starting Email Test ---")
    print(f"EMAIL_HOST: {settings.EMAIL_HOST}")
    print(f"EMAIL_PORT: {settings.EMAIL_PORT}")
    print(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
    print(f"EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
    
    recipient = settings.EMAIL_HOST_USER  # Send to self
    if not recipient:
        print("ERROR: EMAIL_HOST_USER is not set in environment or settings.")
        return

    try:
        print(f"Attempting to send email to {recipient}...")
        send_mail(
            'Test Subject from BioBinConnect Debugger',
            'This is a test email to verify SMTP settings and check for errors.',
            settings.DEFAULT_FROM_EMAIL,
            [recipient],
            fail_silently=False,
        )
        print("✅ SUCCESS: Email sent successfully!")
    except Exception as e:
        print("\n❌ FAILURE: Email sending failed.")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Message: {str(e)}")
        
        # Check for common SMTP codes
        if hasattr(e, 'smtp_code'):
             print(f"SMTP Code: {e.smtp_code}")
        if hasattr(e, 'smtp_error'):
             print(f"SMTP Error: {e.smtp_error}")

if __name__ == "__main__":
    test_email()
