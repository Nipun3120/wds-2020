from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import user_login, trading, home
app_name="tradingclosed"

urlpatterns = [
    path('trading-closed/',trading,name='trading-closed'),
    path('userlogin/',user_login,name='userlogin'),
    path('',home,name="home"),

]