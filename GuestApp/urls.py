from django.urls import path
from GuestApp import views


from GuestApp import views
urlpatterns = [
    path('', views.index, name='guest_index'),
    path('booking/', views.about, name='booking'),
    path('login/', views.login_view, name='login'),
]