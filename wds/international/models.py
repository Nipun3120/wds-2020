from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
#from notifications.models import Notification
#from django.dispatch import receiver
# Create your models here.
stock_list=(
    ('ASHOKLEY','ASHOKLEY'),
    ('WIPRO','WIPRO'),
    ('RAJESHEXPO','RAJESHEXPO'),
    ('AMBUJACEM','AMBUJACEM'),
    ('MM','MM'),
    ('ONGC','ONGC'),
    ('DMART','DMART'),
    ('SUNPHARMA','SUNPHARMA'),
    ('stock9','stock9'),
    ('ADANIPOWER','ADANIPOWER'),
    ('stock11','stock11'),
    ('stock12','stock12'),
    ('stock13','stock13'),
    ('stock14','stock14'),
    ('stock15','stock15'),
)
status_list=(
    ('accepted','accepted'),
    ('declined','declined'),
    ('pending','pending'),
    ('cancelled','cancelled'),
)
action_list=(
    ('buy','buy'),
    ('sell','sell')
)

class StockList(models.Model):
    stockattribute = models.CharField(max_length=20)
    stockname = models.CharField(max_length=100)
    stockprice = models.FloatField(default=0)
    def __str__(self):
        return f"{self.stockname}"


class Stock(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,related_name='inter' ,on_delete=models.CASCADE, default=1)
    ASHOKLEY=models.IntegerField(default=0)
    WIPRO=models.IntegerField(default=0)
    RAJESHEXPO=models.IntegerField(default=0)
    AMBUJACEM=models.IntegerField(default=0)
    MM=models.IntegerField(default=0)
    ONGC=models.IntegerField(default=0)
    DMART=models.IntegerField(default=0)
    SUNPHARMA=models.IntegerField(default=0)
    stock9=models.IntegerField(default=0)
    ADANIPOWER=models.IntegerField(default=0)
    userbalance=models.FloatField(default=1000000.0)
    def __str__(self):
        return f"{self.user}"
        
class trade(models.Model):
    seller=models.ForeignKey(settings.AUTH_USER_MODEL, related_name='seller_of_stock_international',on_delete=models.CASCADE)
    stock=models.CharField(choices=stock_list,max_length=100)
    numberofstocks=models.IntegerField(default=0)
    priceperstock=models.FloatField(null=True, blank=True)
    buyer=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='buyer_of_stock_international', on_delete=models.CASCADE)
    #userbalance=models.FloatField(default=1000000.0)
    

def create_stock(sender,instance,created,**kwargs):
    if created:
        Stock.objects.create(user=instance)

post_save.connect(create_stock,sender=User)



class tradereq(models.Model):
    sender=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender_trade_inter")
    receiver=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver_trade_inter")
    action=models.CharField(choices=action_list,max_length=10,default='buy')
    status=models.CharField(choices=status_list,max_length=50,default='pending')
    stock=models.CharField(choices=stock_list,max_length=100)
    numberofstocks=models.IntegerField(default=0)
    priceperstock=models.FloatField(null=True, blank=False)
    is_active= models.BooleanField(blank=False, null=False, default=True)
    
    def __str__(self):
        return self.sender.username
    def accept(self):
        receiver_stock=Stock.objects.get(user=self.receiver)
        sender_stock=Stock.objects.get(user=self.sender)
        amount=self.numberofstocks*self.priceperstock
        if self.action=='buy':
            sender_stock.userbalance=sender_stock.userbalance-amount
            receiver_stock.userbalance=receiver_stock.userbalance+amount
            if self.stock=='ASHOKLEY':
                if (receiver_stock.ASHOKLEY>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.ASHOKLEY=sender_stock.ASHOKLEY+self.numberofstocks
                        receiver_stock.ASHOKLEY=receiver_stock.ASHOKLEY-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='WIPRO':
                if (receiver_stock.WIPRO>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.WIPRO=sender_stock.WIPRO+self.numberofstocks
                        receiver_stock.WIPRO=receiver_stock.WIPRO-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='RAJESHEXPO':
                if (receiver_stock.RAJESHEXPO>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.RAJESHEXPO=sender_stock.RAJESHEXPO+self.numberofstocks
                        receiver_stock.RAJESHEXPO=receiver_stock.RAJESHEXPO-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='AMBUJACEM':
                if (receiver_stock.AMBUJACEM>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.AMBUJACEM=sender_stock.AMBUJACEM+self.numberofstocks
                        receiver_stock.AMBUJACEM=receiver_stock.AMBUJACEM-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='MM':
                if (receiver_stock.MM>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.ASHOKLEY=sender_stock.MM+self.numberofstocks
                        receiver_stock.MM=receiver_stock.MM-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='ONGC':
                if (receiver_stock.ONGC>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.ONGC=sender_stock.ONGC+self.numberofstocks
                        receiver_stock.ONGC=receiver_stock.ONGC-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='DMART':
                if (receiver_stock.DMART>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.DMART=sender_stock.DMART+self.numberofstocks
                        receiver_stock.DMART=receiver_stock.DMART-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='SUNPHARMA':
                if (receiver_stock.SUNPHARMA>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.SUNPHARMA=sender_stock.SUNPHARMA+self.numberofstocks
                        receiver_stock.SUNPHARMA=receiver_stock.SUNPHARMA-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock9':
                if (receiver_stock.stock9>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock9=sender_stock.stock9+self.numberofstocks
                        receiver_stock.stock9=receiver_stock.stock9-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='ADANIPOWER':
                if (receiver_stock.ADANIPOWER>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.ADANIPOWER=sender_stock.ADANIPOWER+self.numberofstocks
                        receiver_stock.ADANIPOWER=receiver_stock.ADANIPOWER-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            
            receiver_stock.save()
            sender_stock.save()
        elif self.action=='sell':
            sender_stock,receiver_stock=receiver_stock,sender_stock
            if (amount<=receiver_stock.userbalance):
                
                sender_stock.userbalance=sender_stock.userbalance-amount
                receiver_stock.userbalance=receiver_stock.userbalance+amount
                if self.stock=='ASHOKLEY':
                    if(sender_stock.ASHOKLEY>=self.numberofstocks):
                        sender_stock.ASHOKLEY=sender_stock.ASHOKLEY+self.numberofstocks
                        receiver_stock.ASHOKLEY=receiver_stock.ASHOKLEY-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='WIPRO':
                    if(sender_stock.WIPRO>=self.numberofstocks):
                        sender_stock.WIPRO=sender_stock.WIPRO+self.numberofstocks
                        receiver_stock.WIPRO=receiver_stock.WIPRO-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='RAJESHEXPO':
                    if(sender_stock.RAJESHEXPO>=self.numberofstocks):
                        sender_stock.RAJESHEXPO=sender_stock.RAJESHEXPO+self.numberofstocks
                        receiver_stock.RAJESHEXPO=receiver_stock.RAJESHEXPO-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='AMBUJACEM':
                    if(sender_stock.AMBUJACEM>=self.numberofstocks):
                        sender_stock.AMBUJACEM=sender_stock.AMBUJACEM+self.numberofstocks
                        receiver_stock.AMBUJACEM=receiver_stock.AMBUJACEM-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='MM':
                    if(sender_stock.MM>=self.numberofstocks):
                        sender_stock.MM=sender_stock.MM+self.numberofstocks
                        receiver_stock.MM=receiver_stock.MM-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='ONGC':
                    if(sender_stock.ONGC>=self.numberofstocks):
                        sender_stock.ONGC=sender_stock.ONGC+self.numberofstocks
                        receiver_stock.ONGC=receiver_stock.ONGC-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='DMART':
                    if(sender_stock.DMART>=self.numberofstocks):
                        sender_stock.DMART=sender_stock.DMART+self.numberofstocks
                        receiver_stock.DMART=receiver_stock.DMART-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='SUNPHARMA':
                    if(sender_stock.SUNPHARMA>=self.numberofstocks):
                        sender_stock.SUNPHARMA=sender_stock.SUNPHARMA+self.numberofstocks
                        receiver_stock.SUNPHARMA=receiver_stock.SUNPHARMA-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock9':
                    if(sender_stock.stock9>=self.numberofstocks):
                        sender_stock.stock9=sender_stock.stock9+self.numberofstocks
                        receiver_stock.stock9=receiver_stock.stock9-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='ADANIPOWER':
                    if(sender_stock.ADANIPOWER>=self.numberofstocks):
                        sender_stock.ADANIPOWER=sender_stock.ADANIPOWER+self.numberofstocks
                        receiver_stock.ADANIPOWER=receiver_stock.ADANIPOWER-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                self.is_active=False
                self.status='accepted'
            else:
                return ('Insufficient Balance')
            
            receiver_stock.save()
            sender_stock.save()
        #self.is_active=False
        #self.status="accepted"
        print(self.status)
        trading=trade.objects.create(
                    seller=self.receiver,
                    stock=self.stock,
                    numberofstocks=self.numberofstocks,
                    priceperstock=self.priceperstock,
                    buyer=self.sender,
                    #userbalance=userbalance,
                )
        self.save()
    def decline(self):
        self.is_active=False
        self.status="declined"
        print(self.status)
        self.save()

    def cancel(self):
        self.is_active=False
        self.status="cancelled"
        print(self.status)
        self.save()

class Report(models.Model):
    reporter=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reporter_inter")
    reporting=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.reporter}"