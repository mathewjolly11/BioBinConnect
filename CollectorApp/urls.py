from django.urls import path
from CollectorApp import views

urlpatterns = [
    path('dashboard/', views.collector_dashboard, name='collector_dashboard'),
    path('profile/', views.collector_profile, name='collector_profile'),
    path('profile/edit/', views.edit_profile, name='collector_edit_profile'),
]
