from django.urls import path
from CompostManagerApp import views

urlpatterns = [
    path('dashboard/', views.compost_manager_dashboard, name='compost_manager_dashboard'),
    path('waste-inventory/', views.view_waste_inventory, name='waste_inventory'),
    path('create-batch/', views.create_compost_batch, name='create_batch'),
    path('manage-batches/', views.manage_batches, name='manage_batches'),
    path('update-batch/<int:batch_id>/', views.update_batch_status, name='update_batch_status'),
    path('edit-batch/<int:batch_id>/', views.edit_batch, name='edit_batch'),
    path('profile/', views.compost_manager_profile, name='compost_manager_profile'),
    path('profile/edit/', views.edit_profile, name='compost_manager_edit_profile'),
    path('profile/delete/', views.delete_account, name='compost_manager_delete_account'),
    
    # Info pages
    path('services/', views.services, name='compost_manager_services'),
    path('contact/', views.contact, name='compost_manager_contact'),
    path('about/', views.about_us, name='compost_manager_about'),
]
