from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test_email(request):
    """Test page for sending emails"""
    if request.method == 'POST':
        recipient_email = request.POST.get('recipient_email')
        
        if not recipient_email:
            return JsonResponse({
                'success': False,
                'error': 'Please provide a recipient email address'
            })
        
        try:
            # Send test email
            send_mail(
                subject='BioBinConnect - Test Email',
                message='This is a test email from BioBinConnect. If you received this, your email configuration is working correctly!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient_email],
                fail_silently=False,
            )
            
            return JsonResponse({
                'success': True,
                'message': f'Test email sent successfully to {recipient_email}!'
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    # GET request - show the test form
    context = {
        'email_host_user': settings.EMAIL_HOST_USER,
        'email_backend': settings.EMAIL_BACKEND,
    }
    return render(request, 'Admin/test_email.html', context)
