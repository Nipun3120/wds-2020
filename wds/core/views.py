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
from .forms import RegisterForm,tradeform,requestsellform
from django.urls import reverse
from .models import Stock,trade,stock_list, traderequest, TradeList
import json
from .utils import get_trade_request_or_false
from .trade_request_status import TradeRequestStatus
def home(request):
    return render(request,"home.html")


def register(request):
    form=RegisterForm()
    if request.method=="POST":
        form=RegisterForm(data=request.POST)

        if (form.is_valid()):
            user=form.save()
            user.set_password(user.password)
            user.save()
            return redirect("/")
        else:
            print(form.errors)
    else:
        form=RegisterForm()
        
    return render(request, 'register.html', {'form': form})

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
        return redirect('/')
    else:
        print("render part ran successfully")
        return render(request,'userlogin.html')

@login_required
def userlogout(request):
    print("logout")
    logout(request)
    return redirect('/')

@login_required
def dashboard(request):
    user_dashdata = Stock.objects.filter(user=request.user)
    dash_dic = {'dashdata':user_dashdata}
    return render(request,'dashboard.html', {'dashdata':user_dashdata})

posts = [
    {
        'stockname': stock_list[0][0],
        'price': '50000',
    },
    {
        'stockname': stock_list[1][0],
        'price': '30000',
    },
    {
        'stockname': stock_list[2][0],
        'price': '25000',
    },
    {
        'stockname': stock_list[3][0],
        'price': '37000',
    },
    {
        'stockname': stock_list[4][0],
        'price': '30000',
    },
    {
        'stockname': stock_list[5][0],
        'price': '10000',
    },
    {
        'stockname': stock_list[6][0],
        'price': '15000',
    },
    {
        'stockname': stock_list[7][0],
        'price': '60000',
    },
    {
        'stockname': stock_list[8][0],
        'price': '20000',
    },
    {
        'stockname': stock_list[9][0],
        'price': '35000',
    },

]

def stock_display(request):
    context = {
      'posts': posts
    }
    return render(request,'stocks.html', context)


class Trade(ListView):
    def get(self, *args, **kwargs):
        form = tradeform()
        context = {
            'form':form,
        }
        return render(self.request, 'buy-sell-form.html', context)

    def post(self, *args, **kwargs):
        form = tradeform(self.request.POST or None)
        try:
            if form.is_valid():
                seller=form.cleaned_data.get('seller')
                stock=form.cleaned_data.get('stock')
                numberofstocks=form.cleaned_data.get('numberofstocks')
                priceperstock=form.cleaned_data.get('priceperstock')
               # userbalance=form.cleaned_data.get('userbalance')
                buyer=form.cleaned_data.get('buyer')
                trading=trade.objects.create(
                    seller=seller,
                    stock=stock,
                    numberofstocks=numberofstocks,
                    priceperstock=priceperstock,
                    buyer=buyer,
                    #userbalance=userbalance,
                )
                print(priceperstock)
                print(numberofstocks)
                stock_seller=Stock.objects.get(user=seller)
                print(stock_seller)
                          
                stock_buyer=Stock.objects.get(user=buyer)
                print(stock_buyer)
                '''for st in stock_list:
                    if stock==st[0]:
                        stock_seller.st[0]-=numberofstocks
                        stock_seller.userbalance+=priceperstock*numberofstocks
                        stock_buyer.st[0]+=numberofstocks
                        stock_buyer.userbalance-=priceperstock*numberofstocks
                        stock_seller.save()
                        stock_buyer.save()'''

                if stock=="stock1":
                    stock_seller.stock1-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.stock1+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()                 
                    stock_buyer.save()
                elif stock=="stock2":
                    stock_seller.stock2-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.stock2+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()         
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="stock3":
                    stock_seller.stock3-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.stock3+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="stock4":
                    stock_seller.stock4-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.stock4+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="stock5":
                    stock_seller.stock5-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.stock5+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="stock6":
                    stock_seller.stock6-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.stock6+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="stock7":
                    stock_seller.stock7-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.stock7+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="stock8":
                    stock_seller.stock8-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.stock8+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="stock9":
                    stock_seller.stock9-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.stock9+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="stock10":
                    stock_seller.stock10-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.stock10+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                return redirect('/')
        except ObjectDoesNotExist:
                messages.error(self.request, "fill the form correctly")
                return redirect("/")

def request_view(request, *arg, **kwargs):
    context = {}
    user = request.user
    if user.is_authenticated:
        trade_request = traderequest.objects.filter(receiver=user, is_active=True)
        context = {
            'trade_request' : trade_request
        }
    return render(request, "notifications.html", context)



class sellrequest(ListView):
    def get(self, *args, **kwargs):
        form = requestsellform()
        context = {
            'form':form,
        }
        return render(self.request, 'sell-form.html', context)

    def post(self, *args, **kwargs):
        form = requestsellform(self.request.POST or None)
        try:
            if form.is_valid():
                seller=self.request.user
                stock=form.cleaned_data.get('stock')
                numberofstocks=form.cleaned_data.get('numberofstocks')
                priceperstock=form.cleaned_data.get('priceperstock')
               # userbalance=form.cleaned_data.get('userbalance')
                buyer=form.cleaned_data.get('buyer')
                trading=trade.objects.create(
                    seller=seller,
                    stock=stock,
                    numberofstocks=numberofstocks,
                    priceperstock=priceperstock,
                    buyer=buyer,
                    #userbalance=userbalance,
                )
                print(priceperstock)
                print(numberofstocks)
                stock_seller=Stock.objects.get(user=seller)
                print(stock_seller)
                          
                stock_buyer=Stock.objects.get(user=buyer)
                print(stock_buyer)

                payload = {}
        
                user_id = buyer
                if user_id:
                    receiver = Stock.objects.get(user=buyer)
                    try:
                        trade_request = traderequest.objects.filter(sender=seller, receiver=receiver)
                        try:
                            for request in trade_request:
                                if request.is_active:
                                    raise Exception("You already sent them a friend request")

                            trade_request = traderequest(sender=seller, receiver=receiver)
                            trade_request.save()
                            payload['response'] = "Request Sent"
                        except Exception as e:
                            payload['response'] = str(e)
                    except traderequest.DoesNotExist:
                        trade_request = traderequest(sender=seller, receiver=receiver)
                        trade_request.save()
                        payload['response'] = "Request sent"

                    if payload['response'] == None:
                        payload['response'] = "Something Went Wrong"

                else:
                    payload['response'] = "Unable to send request"
                return HttpResponse(json.dumps(payload), content_type="application/json")

                return redirect('/')
        except ObjectDoesNotExist:
                messages.error(self.request, "fill the form correctly")
                return redirect("/")
    
        
        
    



def accept(sender, receiver, is_active):
    if is_active:
        """Call transaction"""


def decline(sender, receiver, is_active):
    is_active=False

'''
def send_sell_request(request, *args, **kwargs):
    user = request.user
    payload = {}
    if request.method == "POST" and user.is_authenticated:
        user_id = request.POST.get("receiver_user_id")
        if user_id:
            receiver = Stock.objects.get(pk=user_id)
            try:
                trade_request = traderequest.objects.filter(sender=user, receiver=receiver)
                try:
                    for request in trade_request:
                        if request.is_active:
                            raise Exception("You already sent them a friend request")

                    trade_request = traderequest(sender=user, receiver=receiver)
                    trade_request.save()
                    payload['response'] = "Request Sent"
                except Exception as e:
                    payload['response'] = str(e)
            except traderequest.DoesNotExist:
                trade_request = traderequest(sender=user, receiver=receiver)
                trade_request.save()
                payload['response'] = "Request sent"

            if payload['response'] == None:
                payload['response'] = "Something Went Wrong"

        else:
            payload['response'] = "Unable to send request"
    else:
        payload['response'] = "You must be logged in"
    return HttpResponse(json.dumps(payload), content_type="application/json")
                '''