from django.urls import path
from FarmerApp import views

urlpatterns = [
    path('dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('profile/', views.farmer_profile, name='farmer_profile'),
    path('profile/edit/', views.edit_profile, name='farmer_edit_profile'),
    path('profile/delete/', views.delete_account, name='farmer_delete_account'),
    
    # Waste purchasing URLs
    path('browse-waste/', views.farmer_browse_waste, name='farmer_browse_waste'),
    path('browse-compost/', views.farmer_browse_compost, name='farmer_browse_compost'),
    path('place-order/', views.farmer_place_order, name='farmer_place_order'),
    path('orders/', views.farmer_orders, name='farmer_orders'),
    path('payment/', views.farmer_payment, name='farmer_payment'),
    
    # Info pages
    path('services/', views.services, name='farmer_services'),
    path('contact/', views.contact, name='farmer_contact'),
    path('about/', views.about_us, name='farmer_about'),
]
