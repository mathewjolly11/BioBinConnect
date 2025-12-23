from django.urls import path
from FarmerApp import views

urlpatterns = [
    path('dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('profile/', views.farmer_profile, name='farmer_profile'),
    path('profile/edit/', views.edit_profile, name='farmer_edit_profile'),
]
