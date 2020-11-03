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
from .forms import RegisterForm,tradeform,requestsellform,tradereqform,reportform
from django.urls import reverse
from .models import Stock,trade,stock_list,tradereq,Report,StockList
import json
from django.db.models import Q
def home(request):
    return render(request,"international/home.html", {'messages': messages.get_messages(request)})

def news(request):
    return render(request,"international/news.html")


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
        
    return render(request, 'international/register.html', {'form': form})





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
            return redirect('international:userlogin')
        return redirect('/')
    else:
        print("render part ran successfully")
        return render(request,'international/userlogin.html')

@login_required
def userlogout(request):
    print("logout")
    logout(request)
    return redirect('/')

@login_required
def dashboard(request):
    user_dashdata = Stock.objects.filter(user=request.user)
    dash_dic = {'dashdata':user_dashdata}
    return render(request,'international/dashboard.html', {'dashdata':user_dashdata})

def stock_display(request):
    context = {
      'posts': StockList.objects.all()
    }
    return render(request,'international/stocks.html', context)


class Trade(ListView):
    def get(self, *args, **kwargs):
        form = tradeform()
        context = {
            'form':form,
        }
        return render(self.request, 'international/buy-sell-form.html', context)

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

                if stock=="JPM":
                    stock_seller.JPM-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.JPM+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()                 
                    stock_buyer.save()
                elif stock=="ATT":
                    stock_seller.ATT-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.ATT+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()         
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="CCA":
                    stock_seller.CCA-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.CCA+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="WMT":
                    stock_seller.WMT-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.WMT+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="JPM":
                    stock_seller.JPM-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.JPM+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="T":
                    stock_seller.T-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.T+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="AER":
                    stock_seller.AER-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.AER+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="BOE":
                    stock_seller.BOE-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.BOE+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="PFZ":
                    stock_seller.PFZ-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.PFZ+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="FBI":
                    stock_seller.FBI-=numberofstocks
                    stock_seller.userbalance+=priceperstock*numberofstocks
                    stock_buyer.FBI+=numberofstocks
                    stock_buyer.userbalance-=priceperstock*numberofstocks
                    stock_seller.save()
                    stock_buyer.save()
                return redirect('/')
        except ObjectDoesNotExist:
                messages.error(self.request, "fill the form correctly")
                return redirect("/")
@login_required
def reqcreate(request):
    user=request.user
    if request.method=='POST':
        form = tradereqform(request.POST or None)
        if form.is_valid():
                sender=user
                receiver=form.cleaned_data.get('receiver')
                action=form.cleaned_data.get('action')
                stock=form.cleaned_data.get('stock')
                numberofstock=form.cleaned_data.get('numberofstocks')
                priceperstock=form.cleaned_data.get('priceperstock')
                amount = numberofstock*priceperstock
                stock_request_sender=Stock.objects.get(user=sender)
                status='pending'
                if action=='buy':
                    if (amount<=stock_request_sender.userbalance):
                        request_trade=tradereq.objects.create(
                            sender=sender,
                            receiver=receiver,action=action,
                            stock=stock,
                            numberofstocks=numberofstock,
                            priceperstock=priceperstock,
                            is_active=True,
                        )
                        return redirect('international:sentreq')
                    else:
                        messages.error(request, f'Insufficient Balance for transaction!!')
                elif action=='sell':
                    if stock=='JPM':
                        if (numberofstock<=stock_request_sender.JPM):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('international:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='ATT':
                        if (numberofstock<=stock_request_sender.ATT):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('international:sentreq')
                        else:
                             messages.warning(request, f'Insufficient Stock holdings!!')
                    elif stock=='CCA':
                        if (numberofstock<=stock_request_sender.CCA):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('international:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='WMT':
                        if (numberofstock<=stock_request_sender.WMT):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('international:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='AER':
                        if (numberofstock<=stock_request_sender.AER):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('international:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='BOE':
                        if (numberofstock<=stock_request_sender.BOE):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('international:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='PFZ':
                        if (numberofstock<=stock_request_sender.PFZ):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('international:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='FBI':
                        if (numberofstock<=stock_request_sender.FBI):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('international:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')              
                    elif stock=='ZVC':
                        if (numberofstock<=stock_request_sender.ZVC):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('international:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='PAP':
                        if (numberofstock<=stock_request_sender.PAP):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('international:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='TXT':
                        if (numberofstock<=stock_request_sender.TXT):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('international:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='GMS':
                        if (numberofstock<=stock_request_sender.GMS):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('international:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='APL':
                        if (numberofstock<=stock_request_sender.APL):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('international:sentreq')
                        else:
                            messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='TES':
                        if (numberofstock<=stock_request_sender.TES):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('international:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    elif stock=='INT':
                        if (numberofstock<=stock_request_sender.INT):
                            request_trade=tradereq.objects.create(
                                sender=sender,
                                receiver=receiver,action=action,
                                stock=stock,
                                numberofstocks=numberofstock,
                                priceperstock=priceperstock,
                                is_active=True,
                            )
                            return redirect('international:sentreq')
                        else:
                             messages.error(request, f'Insufficient Stock holdings!!')
                    
    return render(request,'international/create_request.html',{'form':tradereqform})
@login_required
def report(request):
    form = reportform()
    if request.method=='POST':
        form = reportform(request.POST or None)
        if form.is_valid():
            obj = Report()
            obj.reporter=request.user
            obj.reporting=form.cleaned_data.get('reporting')
            print(obj.reporter)
            print(obj.reporting)
            obj.save()
        else:
            form=reportform()
        return redirect('international:dashboard')
    return render(request, 'international/report.html', {'form':form})
@login_required
def received_request(request):
    user=request.user
    requests_pending=tradereq.objects.order_by('-id').filter(receiver=user,is_active=True)
    return render(request,'international/received_request.html',{'requests':requests_pending})

@login_required
def sent_request(request):
    user=request.user
    sent_pending=tradereq.objects.order_by('-id').filter(sender=user,is_active=True)
    return render(request,'international/sent_requests.html',{'requests':sent_pending})

@login_required
def history(request):
    user=request.user
    transactions=tradereq.objects.order_by('-id').filter(sender=user)
    return render(request,'international/transaction-history.html',{'requests':transactions})


@login_required
def all_history(request):
    user=request.user
    #transactions=tradereq.objects.order_by('-id').filter(Q(receiver=user) | Q(sender=user))
    comb_query = tradereq.objects.filter(sender=user) | tradereq.objects.filter(receiver=user)
    final_query = comb_query.filter(status='accepted')
    transactions=final_query.order_by('-id')
    return render(request,'international/transaction-log.html',{'requests':transactions})


"""
@login_required
def accept_request(request,*args, **kwargs):
    user=request.user
    payload={}
    if request.method=='GET':
        tradereq_id=kwargs.get("friend_request_id")
        if tradereq_id:
            trade_request=tradereq.objects.id(pk=tradereq_id)
            if trade_request.receiver==user:
                if trade_request:
                    trade_request.accept()
                    payload['response']="request accepted"
                else:
                    payload['response']="something went wrong"
            else:
                payload['response']="not yours request"
        else:
            payload['response']="unable not accepted"
    else:
        payload['response']="you must be authenticated to accpet a friend request"
    return HttpResponse(json.dumps(payload),content_type="application/json")
"""

@login_required 
def accept_request(request,*args, **kwargs):
    user =request.user
    if request.method=='GET':
        tradereq_id=kwargs.get("friend_request_id")
        if tradereq_id:
            trade_request=tradereq.objects.filter(pk=tradereq_id)[0]
            if trade_request:
                mess = trade_request.accept()
                print(mess)
                messages.error(request, mess)
                return redirect("international:receivedreq")

@login_required
def decline_request(request,*args, **kwargs):
    user=request.user
    if request.method=='GET':
        tradereq_id=kwargs.get("friend_request_id")
        if tradereq_id:
            trade_request=tradereq.objects.filter(pk=tradereq_id)[0]
            if trade_request:
                trade_request.decline()
                return redirect("international:receivedreq")


@login_required
def cancel_request(request,*args, **kwargs):
    user=request.user
    if request.method=='GET':
        tradereq_id=kwargs.get("friend_request_id")
        if tradereq_id:
            trade_request=tradereq.objects.filter(pk=tradereq_id)[0]
            if trade_request:
                trade_request.cancel()
                return redirect("international:sentreq")


