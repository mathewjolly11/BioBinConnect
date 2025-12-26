from django.urls import path
from MyApp import views


from MyApp import views
from MyApp import reports_views
from MyApp import payment_views
from MyApp import salary_views
urlpatterns = [
    path('admin', views.index, name='admin_index'),
    path('add_district/', views.add_district, name='add_district'),
    path('view_districts/', views.view_districts, name='view_districts'),
    path('edit_district/<int:district_id>/', views.edit_district, name='edit_district'),
    path('delete_district/<int:district_id>/', views.delete_district, name='delete_district'),
    path('add_location/', views.add_location, name='add_location'),
    path('view_locations/', views.view_locations, name='view_locations'),
    path('edit_location/<int:location_id>/', views.edit_location, name='edit_location'),
    path('delete_location/<int:location_id>/', views.delete_location, name='delete_location'),
    path('add_ra/', views.add_ra, name='add_ra'),
    path('view_ra/', views.view_ra, name='view_ra'),
    path('edit_ra/<int:ra_id>/', views.edit_ra, name='edit_ra'),
    path('delete_ra/<int:ra_id>/', views.delete_ra, name='delete_ra'),
    path('view_users/', views.view_users, name='view_users'),
    path('approve_user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('reject_user/<int:user_id>/', views.reject_user, name='reject_user'),
    path('assign_collector/', views.assign_collector, name='assign_collector'),
    path('view_assignments/', views.view_assignments, name='view_assignments'),
    path('add_route/', views.add_route, name='add_route'),
    path('view_routes/', views.view_routes, name='view_routes'),
    path('payment_report/', views.payment_report, name='payment_report'),
    path('export_payment_report/', views.export_payment_report, name='export_payment_report'),
    
    # Admin sales management
    path('admin/waste-sales/', views.admin_waste_sales, name='admin_waste_sales'),
    path('admin/compost-sales/', views.admin_compost_sales, name='admin_compost_sales'),
    path('admin/update-delivery/<int:order_id>/', views.admin_update_delivery_status, name='admin_update_delivery'),
    
    # Admin reports
    path('admin/reports/', reports_views.admin_reports, name='admin_reports'),
    
    # Payment transactions
    path('admin/payment-transactions/', payment_views.payment_transactions, name='payment_transactions'),
    
    # Manager salaries
    path('admin/manager-salaries/', salary_views.manager_salaries, name='manager_salaries'),
]

