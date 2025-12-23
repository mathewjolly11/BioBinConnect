from django.urls import path
from CollectorApp import views

urlpatterns = [
    path('dashboard/', views.collector_dashboard, name='collector_dashboard'),
    path('profile/', views.collector_profile, name='collector_profile'),
    path('profile/edit/', views.edit_profile, name='collector_edit_profile'),
    path('profile/delete/', views.delete_account, name='collector_delete_account'),
    path('assigned-pickups/', views.view_assigned_pickups, name='view_assigned_pickups'),
    path('log-collection/<int:pickup_id>/', views.log_collection, name='log_collection'),
    path('history/', views.collection_history, name='collection_history'),
]
