import os
import django
import sys

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')
django.setup()

from MyApp.models import SystemSettings
from django.core.mail import send_mail
from django.conf import settings

def verify_toggle():
    print("--- Verifying Email Toggle ---")
    
    # 1. Check initial state
    initial_setting = SystemSettings.get_setting('email_notifications_enabled', 'True')
    print(f"Initial Setting: {initial_setting}")
    
    # 2. Disable Emails
    print("\n[Step 1] Disabling Emails...")
    SystemSettings.set_setting('email_notifications_enabled', 'False')
    
    # 3. Attempt to send email (Should be skipped)
    print("Attempting to send email (Expect SKIPPED)...")
    try:
        from utils.email_service import send_email
        # We use the utility function because that's where the check is implemented
        result = send_email(
            'Test Subject (Disabled)', 
            'emails/household/registration_success.html', # Just a dummy template path 
            {'user_name': 'Test'}, 
            settings.EMAIL_HOST_USER
        )
        print(f"Result: {result}")
        if result == True:
            print("✅ Behavior Correct: Function returned True (simulated success) but check console for 'Skipped' message.")
        else:
            print("❌ Behavior Incorrect: Function returned False.")
            
    except Exception as e:
        print(f"❌ Exception: {e}")

    # 4. Re-enable Emails
    print("\n[Step 2] Re-enabling Emails...")
    SystemSettings.set_setting('email_notifications_enabled', 'True')
    current_setting = SystemSettings.get_setting('email_notifications_enabled')
    print(f"Current Setting: {current_setting}")
    
    if current_setting == 'True':
         print("✅ Toggle successfully reset to Enabled.")
    else:
         print("❌ Failed to reset toggle.")

if __name__ == "__main__":
    verify_toggle()
