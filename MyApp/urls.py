from django.urls import path
from MyApp import views
from MyApp import reports_views
from MyApp import payment_views
from MyApp import salary_views
from MyApp import sales_views
urlpatterns = [
    path('', views.index, name='admin_index'),  # Changed from 'admin' to '' since admin/ is already in main urls
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
    path('approve_all_users/', views.approve_all_users, name='approve_all_users'),
    path('reject_all_users/', views.reject_all_users, name='reject_all_users'),
    path('assign_collector/', views.assign_collector, name='assign_collector'),
    path('view_assignments/', views.view_assignments, name='view_assignments'),
    path('delete_assignment/<int:assignment_id>/', views.delete_assignment, name='delete_assignment'),
    path('add_route/', views.add_route, name='add_route'),
    path('view_routes/', views.view_routes, name='view_routes'),
    path('payment_report/', views.payment_report, name='payment_report'),
    path('export_payment_report/', views.export_payment_report, name='export_payment_report'),
    
    
    # Admin sales management
    path('waste-sales/', sales_views.admin_waste_sales, name='admin_waste_sales'),
    path('assign-collector/<int:order_id>/', sales_views.assign_waste_collector, name='assign_waste_collector'),
    path('auto-assign-collector/<int:order_id>/', sales_views.auto_assign_waste_collector, name='auto_assign_waste_collector'),
    path('toggle-auto-assignment/', sales_views.toggle_auto_assignment, name='toggle_auto_assignment'),
    path('compost-sales/', sales_views.admin_compost_sales, name='admin_compost_sales'),
    path('update-delivery/<int:order_id>/', sales_views.admin_update_delivery_status, name='admin_update_delivery'),
    path('stock-management/', sales_views.admin_stock_management, name='admin_stock_management'),


    
    # Salary management
    path('salaries/', salary_views.admin_salary_management, name='admin_salary_management'),
    path('pay-salary/', salary_views.admin_pay_salary, name='admin_pay_salary'),
    path('pay-confirm/<str:user_type>/<int:user_id>/', salary_views.pay_salary_confirm, name='pay_salary_confirm'),
    
    # Admin reports
    path('reports/', reports_views.admin_reports, name='admin_reports'),
    
    # Payment transactions
    path('payment-transactions/', payment_views.payment_transactions, name='payment_transactions'),
    path('payment-revenue-analytics/', payment_views.payment_revenue_analytics, name='payment_revenue_analytics'),
    
    # Manager salaries
    path('manager-salaries/', salary_views.manager_salaries, name='manager_salaries'),
    
    # Collector salaries
    path('collector-salaries/', payment_views.collector_salaries, name='collector_salaries'),
    
    # Admin profile
    path('profile/', views.admin_profile, name='admin_profile'),
    
    # View Aadhaar image
    path('view_aadhaar/<int:user_id>/', views.view_aadhaar, name='view_aadhaar'),
    
    # Bin type management
    path('add_bin_type/', views.add_bin_type, name='add_bin_type'),
    path('view_bin_types/', views.view_bin_types, name='view_bin_types'),
    path('edit_bin_type/<int:bin_type_id>/', views.edit_bin_type, name='edit_bin_type'),
    path('delete_bin_type/<int:bin_type_id>/', views.delete_bin_type, name='delete_bin_type'),
    
    # User management
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('change_user_password/<int:user_id>/', views.change_user_password, name='change_user_password'),
    
    # System settings
    path('settings/', views.admin_settings, name='admin_settings'),
]

