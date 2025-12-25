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
    path('waste-inventory/', views.collector_waste_inventory, name='collector_waste_inventory'),
    path('sales-orders/', views.collector_sales_orders, name='collector_sales_orders'),
    path('update-delivery/<int:supply_id>/', views.update_delivery_status, name='update_delivery_status'),
]
