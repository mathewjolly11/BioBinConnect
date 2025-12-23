from django.urls import path
from HouseholdApp import views

urlpatterns = [
    path('dashboard/', views.household_dashboard, name='household_dashboard'),
    path('profile/', views.household_profile, name='household_profile'),
    path('profile/edit/', views.edit_profile, name='household_edit_profile'),
]
