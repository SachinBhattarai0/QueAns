from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('register/',views.registerPage,name='register'),
    path('logout/',views.logoutPage,name='logout'),
    path('edit-profile/',views.editProfile,name='editprofile'),
    path('profile/<str:pk>/',views.profile,name='profile'),
]