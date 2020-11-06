from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import home
from tradingclosed import views
app_name="tradingclosed"

urlpatterns = [
    path('trading-closed/',views.closetemplate,name='trading-closed'),
    path('userlogin/',views.user_login,name='userlogin'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('news/',views.news,name='news'),
    path('',home,name="home"),

]