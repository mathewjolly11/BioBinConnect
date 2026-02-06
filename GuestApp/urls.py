from django.urls import path
from GuestApp import views
from GuestApp import api_views
from GuestApp import password_reset_views


urlpatterns = [
    path('', views.index, name='guest_index'),
    path('booking/', views.about, name='booking'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('services/', views.services, name='guest_services'),
    path('contact/', views.contact, name='guest_contact'),
    path('about/', views.about_us, name='guest_about'),
    path('faq/', views.faq, name='guest_faq'),
    path('how-it-works/', views.how_it_works, name='guest_how_it_works'),
    
    # Demo page for testing validations
    path('validation-demo/', views.validation_demo, name='validation_demo'),
    
    # Voice accessibility test page
    path('test-voice/', views.test_voice, name='test_voice'),
    
    # Password Reset URLs
    path('forgot-password/', password_reset_views.forgot_password_request, name='forgot_password_request'),
    path('verify-otp/', password_reset_views.verify_otp, name='verify_otp'),
    path('resend-otp/', password_reset_views.resend_otp, name='resend_otp'),
    path('reset-password/', password_reset_views.reset_password, name='reset_password'),
    
    # API endpoints
    path('api/validate-house-number/', api_views.validate_house_number, name='validate_house_number'),
    path('api/get-next-house-number/', api_views.get_next_house_number, name='get_next_house_number'),
]

