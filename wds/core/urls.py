from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, Trade
from core import views
app_name="core"

urlpatterns = [
    
    path('register/',views.register,name='register'),
    path('userlogin/',views.user_login,name='userlogin'),
    path('stocks/',views.stock_display,name='stocks'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('news/',views.news,name='news'),
    path('buy-sell-form/',Trade.as_view(),name='buy-sell-form'),
    path('',home,name="home"),
    
]
