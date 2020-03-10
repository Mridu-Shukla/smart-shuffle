from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="user_login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/profile/', views.profile, name="profile"),
    path('dashboard/profile/edit_pic/', views.edit_pic, name="edit_pic"),
    path('dashboard/profile/edit_profile/', views.edit_profile, name="edit_profile"),
    path('favourites/<int:id>', views.addFav, name="fav_song"),
    path('favourites/', views.favourite, name="fav_songs"),
    path('playlist/', views.playlist, name="playlist"),
] 

