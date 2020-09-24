from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import home
from core import views
app_name="core"

urlpatterns = [
    
    path('register/',views.register,name='register'),
    path('userlogin/',views.user_login,name='userlogin'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('',home,name="home"),
    
]
