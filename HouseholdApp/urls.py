from django.urls import path
from HouseholdApp import views

urlpatterns = [
    path('dashboard/', views.household_dashboard, name='household_dashboard'),
    path('profile/', views.household_profile, name='household_profile'),
    path('profile/edit/', views.edit_profile, name='household_edit_profile'),
    path('profile/delete/', views.delete_account, name='household_delete_account'),
    path('request-pickup/', views.request_pickup, name='request_pickup'),
    path('my-requests/', views.view_requests, name='view_requests'),
    path('make-payment/', views.make_payment, name='make_payment'),
    path('payment-history/', views.payment_history, name='payment_history'),
    path('services/', views.services, name='household_services'),
    path('contact/', views.contact, name='household_contact'),
]
