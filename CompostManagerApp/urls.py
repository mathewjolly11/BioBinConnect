from django.urls import path
from CompostManagerApp import views

urlpatterns = [
    path('dashboard/', views.compost_manager_dashboard, name='compost_manager_dashboard'),
    path('profile/', views.compost_manager_profile, name='compost_manager_profile'),
    path('profile/edit/', views.edit_profile, name='compost_manager_edit_profile'),
]
