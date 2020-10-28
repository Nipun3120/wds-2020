from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, Trade, reqcreate,received_request,sent_request,accept_request,decline_request,cancel_request,report
from core import views
app_name="core"

urlpatterns = [
    
    path('register/',views.register,name='register'),
    path('userlogin/',views.user_login,name='userlogin'),
    path('stocks/',views.stock_display,name='stocks'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('news/',views.news,name='news'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('news/',views.news,name='news'),
    path('buy-sell-form/',Trade.as_view(),name='buy-sell-form'),
    path('reqcreate/',reqcreate,name='createrequest'),
    path('receivedreq/',received_request,name='receivedreq'),
    path('sentreq/',sent_request,name='sentreq'),
    path('report/',report,name='report'),
    path('accept_request/<friend_request_id>',accept_request,name='accept-request'),
    path('decline_request/<friend_request_id>',decline_request,name='decline-request'),
    path('cancel_request/<friend_request_id>',cancel_request,name='cancel-request'),
    path('',home,name="home"),
    
]
