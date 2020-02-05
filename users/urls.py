from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="user_login"),
    path('dashboard/', views.dashboard, name="dashboard"),
] 
