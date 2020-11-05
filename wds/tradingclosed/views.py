from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from  django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request,"tradingclosed/home.html")

def closetemplate(request):
    return render(request,"tradingclosed/trading-closed.html")

def news(request):
    return render(request,"tradingclosed/news.html")
    
def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)


        user=authenticate(username=username,password=password)

        if user is not None:
                login(request,user)
        else:
            print("false login")
            messages.error(request, f'Invalid Teamname or Password')
            return redirect('tradingclosed:userlogin')
        return render(request,'tradingclosed:home')
    else:
        print("render part ran successfully")
        return render(request,'tradingclosed/userlogin.html')


@login_required
def userlogout(request):
    print("logout")
    logout(request)
    return redirect('/')
