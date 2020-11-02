from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.contrib import messages
from  django.http import HttpResponse
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
    ('HINDUUNILVR','HINDUUNILVR'),
    ('ADANIPOWER','ADANIPOWER'),
    ('TATASTEEL','TATASTEEL'),
    ('IOC','IOC'),
    ('JINDALSTL','JINDALSTL'),
    ('INDIAMART','INDIAMART'),
    ('RELIANCE','RELIANCE'),
    ('INFOSYS','INFOSYS'),
    ('BATA','BATA'),
    ('BHARTIARTL','BHARTIARTL'),
    ('MARUTI','MARUTI'),
    ('ITC','ITC'),
    ('HDFCBANK','HDFCBANK'),
    ('IGL','IGL'),
    ('VOLTAS','VOLTAS'),
    ('BAJFINANCE','BAJFINANCE'),
    ('SBI','SBI'),
    ('CIPLA','CIPLA'),
    ('TCS','TCS'),
    ('LT','LT'),
    ('ASIANPAINT','ASIANPAINT'),
    ('ICICIPRULI','ICICIPRULI'),
    ('PVR','PVR'),
    ('PIDILITIND','PIDILITIND'),
    ('TRENT','TRENT'),
    
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
    stockattribute = models.CharField(max_length=20, default="STOCK")
    stockname = models.CharField(max_length=100)
    stockprice = models.FloatField(default=0)

    def __str__(self):
        return f"{self.stockname}"


class Stock(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    ASHOKLEY=models.IntegerField(default=0)
    WIPRO=models.IntegerField(default=0)
    RAJESHEXPO=models.IntegerField(default=0)
    AMBUJACEM=models.IntegerField(default=0)
    MM=models.IntegerField(default=0)
    ONGC=models.IntegerField(default=0)
    DMART=models.IntegerField(default=0)
    SUNPHARMA=models.IntegerField(default=0)
    HINDUUNILVR=models.IntegerField(default=0)
    ADANIPOWER=models.IntegerField(default=0)
    TATASTEEL=models.IntegerField(default=0)
    IOC=models.IntegerField(default=0)
    JINDALSTL=models.IntegerField(default=0)
    INDIAMART=models.IntegerField(default=0)
    RELIANCE=models.IntegerField(default=0)
    INFOSYS=models.IntegerField(default=0)
    BATA=models.IntegerField(default=0)
    BHARTIARTL=models.IntegerField(default=0)
    MARUTI=models.IntegerField(default=0)
    ITC=models.IntegerField(default=0)
    HDFCBANK=models.IntegerField(default=0)
    IGL=models.IntegerField(default=0)
    VOLTAS=models.IntegerField(default=0)
    BAJFINANCE=models.IntegerField(default=0)
    SBI=models.IntegerField(default=0)
    CIPLA=models.IntegerField(default=0)
    TCS=models.IntegerField(default=0)
    LT=models.IntegerField(default=0)
    ASIANPAINT=models.IntegerField(default=0)
    ICICIPRULI=models.IntegerField(default=0)
    PVR=models.IntegerField(default=0)
    PIDILITIND=models.IntegerField(default=0)
    TRENT=models.IntegerField(default=0)
    
    
    
    userbalance=models.FloatField(default=1000000.0)
    def __str__(self):
        return f"{self.user}"
        
class trade(models.Model):
    seller=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stock=models.CharField(choices=stock_list,max_length=100)
    numberofstocks=models.IntegerField(default=0)
    priceperstock=models.FloatField(null=True, blank=True)
    buyer=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='buyer_of_stock', on_delete=models.CASCADE)
    #userbalance=models.FloatField(default=1000000.0)
    

def create_stock(sender,instance,created,**kwargs):
    if created:
        Stock.objects.create(user=instance)

post_save.connect(create_stock,sender=User)



class tradereq(models.Model):
    sender=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender_trade")
    receiver=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver_trade")
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
            elif self.stock=='HINDUUNILVR':
                if (receiver_stock.HINDUUNILVR>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.HINDUUNILVR=sender_stock.HINDUUNILVR+self.numberofstocks
                        receiver_stock.HINDUUNILVR=receiver_stock.HINDUUNILVR-self.numberofstocks
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
            elif self.stock=='TATASTEEL':
                if (receiver_stock.TATASTEEL>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.TATASTEEL=sender_stock.TATASTEEL+self.numberofstocks
                        receiver_stock.TATASTEEL=receiver_stock.TATASTEEL-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='IOC':
                if (receiver_stock.IOC>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.IOC=sender_stock.IOC+self.numberofstocks
                        receiver_stock.IOC=receiver_stock.IOC-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='JINDALSTL':
                if (receiver_stock.JINDALSTL>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.JINDALSTL=sender_stock.JINDALSTL+self.numberofstocks
                        receiver_stock.JINDALSTL=receiver_stock.JINDALSTL-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='INDIAMART':
                if (receiver_stock.INDIAMART>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.INDIAMART=sender_stock.INDIAMART+self.numberofstocks
                        receiver_stock.INDIAMART=receiver_stock.INDIAMART-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='RELIANCE':
                if (receiver_stock.RELIANCE>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.RELIANCE=sender_stock.RELIANCE+self.numberofstocks
                        receiver_stock.RELIANCE=receiver_stock.RELIANCE-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='INFOSYS':
                if (receiver_stock.INFOSYS>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.INFOSYS=sender_stock.INFOSYS+self.numberofstocks
                        receiver_stock.INFOSYS=receiver_stock.INFOSYS-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='BATA':
                if (receiver_stock.BATA>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.BATA=sender_stock.BATA+self.numberofstocks
                        receiver_stock.BATA=receiver_stock.BATA-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='BHARTIARTL':
                if (receiver_stock.BHARTIARTL>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.BHARTIARTL=sender_stock.BHARTIARTL+self.numberofstocks
                        receiver_stock.BHARTIARTL=receiver_stock.BHARTIARTL-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='MARUTI':
                if (receiver_stock.MARUTI>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.MARUTI=sender_stock.MARUTI+self.numberofstocks
                        receiver_stock.MARUTI=receiver_stock.MARUTI-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='ITC':
                if (receiver_stock.ITC>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.ITC=sender_stock.ITC+self.numberofstocks
                        receiver_stock.ITC=receiver_stock.ITC-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='HDFCBANK':
                if (receiver_stock.HDFCBANK>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.HDFCBANK=sender_stock.HDFCBANK+self.numberofstocks
                        receiver_stock.HDFCBANK=receiver_stock.HDFCBANK-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='IGL':
                if (receiver_stock.IGL>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.IGL=sender_stock.IGL+self.numberofstocks
                        receiver_stock.IGL=receiver_stock.IGL-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='VOLTAS':
                if (receiver_stock.VOLTAS>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.VOLTAS=sender_stock.VOLTAS+self.numberofstocks
                        receiver_stock.VOLTAS=receiver_stock.VOLTAS-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='BAJFINANCE':
                if (receiver_stock.BAJFINANCE>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.BAJFINANCE=sender_stock.BAJFINANCE+self.numberofstocks
                        receiver_stock.BAJFINANCE=receiver_stock.BAJFINANCE-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='SBI':
                if (receiver_stock.SBI>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.SBI=sender_stock.SBI+self.numberofstocks
                        receiver_stock.SBI=receiver_stock.SBI-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='CIPLA':
                if (receiver_stock.CIPLA>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.CIPLA=sender_stock.CIPLA+self.numberofstocks
                        receiver_stock.CIPLA=receiver_stock.CIPLA-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='TCS':
                if (receiver_stock.TCS>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.TCS=sender_stock.TCS+self.numberofstocks
                        receiver_stock.TCS=receiver_stock.TCS-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='LT':
                if (receiver_stock.LT>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.LT=sender_stock.LT+self.numberofstocks
                        receiver_stock.LT=receiver_stock.LT-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='ASIANPAINT':
                if (receiver_stock.ASIANPAINT>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.ASIANPAINT=sender_stock.ASIANPAINT+self.numberofstocks
                        receiver_stock.ASIANPAINT=receiver_stock.ASIANPAINT-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='ICICIPRULI':
                if (receiver_stock.ICICIPRULI>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.ICICIPRULI=sender_stock.ICICIPRULI+self.numberofstocks
                        receiver_stock.ICICIPRULI=receiver_stock.ICICIPRULI-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='PVR':
                if (receiver_stock.PVR>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.PVR=sender_stock.PVR+self.numberofstocks
                        receiver_stock.PVR=receiver_stock.PVR-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='PIDILITIND':
                if (receiver_stock.PIDILITIND>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.PIDILITIND=sender_stock.PIDILITIND+self.numberofstocks
                        receiver_stock.PIDILITIND=receiver_stock.PIDILITIND-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='TRENT':
                if (receiver_stock.TRENT>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.TRENT=sender_stock.TRENT+self.numberofstocks
                        receiver_stock.TRENT=receiver_stock.TRENT-self.numberofstocks
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
                elif self.stock=='HINDUUNILVR':
                    if(sender_stock.HINDUUNILVR>=self.numberofstocks):
                        sender_stock.HINDUUNILVR=sender_stock.HINDUUNILVR+self.numberofstocks
                        receiver_stock.HINDUUNILVR=receiver_stock.HINDUUNILVR-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='ADANIPOWER':
                    if(sender_stock.ADANIPOWER>=self.numberofstocks):
                        sender_stock.ADANIPOWER=sender_stock.ADANIPOWER+self.numberofstocks
                        receiver_stock.ADANIPOWER=receiver_stock.ADANIPOWER-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='TATASTEEL':
                    if(sender_stock.TATASTEEL>=self.numberofstocks):
                        sender_stock.TATASTEEL=sender_stock.TATASTEEL+self.numberofstocks
                        receiver_stock.TATASTEEL=receiver_stock.TATASTEEL-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='IOC':
                    if(sender_stock.IOC>=self.numberofstocks):
                        sender_stock.IOC=sender_stock.IOC+self.numberofstocks
                        receiver_stock.IOC=receiver_stock.IOC-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='JINDALSTL':
                    if(sender_stock.JINDALSTL>=self.numberofstocks):
                        sender_stock.JINDALSTL=sender_stock.JINDALSTL+self.numberofstocks
                        receiver_stock.JINDALSTL=receiver_stock.JINDALSTL-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='INDIAMART':
                    if(sender_stock.INDIAMART>=self.numberofstocks):
                        sender_stock.INDIAMART=sender_stock.INDIAMART+self.numberofstocks
                        receiver_stock.INDIAMART=receiver_stock.INDIAMART-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='RELIANCE':
                    if(sender_stock.RELIANCE>=self.numberofstocks):
                        sender_stock.RELIANCE=sender_stock.RELIANCE+self.numberofstocks
                        receiver_stock.RELIANCE=receiver_stock.RELIANCE-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='INFOSYS':
                    if(sender_stock.INFOSYS>=self.numberofstocks):
                        sender_stock.INFOSYS=sender_stock.INFOSYS+self.numberofstocks
                        receiver_stock.INFOSYS=receiver_stock.INFOSYS-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='BATA':
                    if(sender_stock.BATA>=self.numberofstocks):
                        sender_stock.BATA=sender_stock.BATA+self.numberofstocks
                        receiver_stock.BATA=receiver_stock.BATA-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='BHARTIARTL':
                    if(sender_stock.BHARTIARTL>=self.numberofstocks):
                        sender_stock.BHARTIARTL=sender_stock.BHARTIARTL+self.numberofstocks
                        receiver_stock.BHARTIARTL=receiver_stock.BHARTIARTL-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='MARUTI':
                    if(sender_stock.MARUTI>=self.numberofstocks):
                        sender_stock.MARUTI=sender_stock.MARUTI+self.numberofstocks
                        receiver_stock.MARUTI=receiver_stock.MARUTI-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='ITC':
                    if(sender_stock.ITC>=self.numberofstocks):
                        sender_stock.ITC=sender_stock.ITC+self.numberofstocks
                        receiver_stock.ITC=receiver_stock.ITC-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='HDFCBANK':
                    if(sender_stock.HDFCBANK>=self.numberofstocks):
                        sender_stock.HDFCBANK=sender_stock.HDFCBANK+self.numberofstocks
                        receiver_stock.HDFCBANK=receiver_stock.HDFCBANK-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='IGL':
                    if(sender_stock.IGL>=self.numberofstocks):
                        sender_stock.IGL=sender_stock.IGL+self.numberofstocks
                        receiver_stock.IGL=receiver_stock.IGL-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='VOLTAS':
                    if(sender_stock.VOLTAS>=self.numberofstocks):
                        sender_stock.VOLTAS=sender_stock.VOLTAS+self.numberofstocks
                        receiver_stock.VOLTAS=receiver_stock.VOLTAS-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='BAJFINANCE':
                    if(sender_stock.BAJFINANCE>=self.numberofstocks):
                        sender_stock.BAJFINANCE=sender_stock.BAJFINANCE+self.numberofstocks
                        receiver_stock.BAJFINANCE=receiver_stock.BAJFINANCE-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='SBI':
                    if(sender_stock.SBI>=self.numberofstocks):
                        sender_stock.SBI=sender_stock.SBI+self.numberofstocks
                        receiver_stock.SBI=receiver_stock.SBI-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='CIPLA':
                    if(sender_stock.CIPLA>=self.numberofstocks):
                        sender_stock.CIPLA=sender_stock.CIPLA+self.numberofstocks
                        receiver_stock.CIPLA=receiver_stock.CIPLA-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='TCS':
                    if(sender_stock.TCS>=self.numberofstocks):
                        sender_stock.TCS=sender_stock.TCS+self.numberofstocks
                        receiver_stock.TCS=receiver_stock.TCS-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='LT':
                    if(sender_stock.LT>=self.numberofstocks):
                        sender_stock.LT=sender_stock.LT+self.numberofstocks
                        receiver_stock.LT=receiver_stock.LT-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='ASIANPAINT':
                    if(sender_stock.ASIANPAINT>=self.numberofstocks):
                        sender_stock.ASIANPAINT=sender_stock.ASIANPAINT+self.numberofstocks
                        receiver_stock.ASIANPAINT=receiver_stock.ASIANPAINT-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='ICICIPRULI':
                    if(sender_stock.ICICIPRULI>=self.numberofstocks):
                        sender_stock.ICICIPRULI=sender_stock.ICICIPRULI+self.numberofstocks
                        receiver_stock.ICICIPRULI=receiver_stock.ICICIPRULI-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='PVR':
                    if(sender_stock.PVR>=self.numberofstocks):
                        sender_stock.PVR=sender_stock.PVR+self.numberofstocks
                        receiver_stock.PVR=receiver_stock.PVR-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='PIDILITIND':
                    if(sender_stock.PIDILITIND>=self.numberofstocks):
                        sender_stock.PIDILITIND=sender_stock.PIDILITIND+self.numberofstocks
                        receiver_stock.PIDILITIND=receiver_stock.PIDILITIND-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='TRENT':
                    if(sender_stock.TRENT>=self.numberofstocks):
                        sender_stock.TRENT=sender_stock.TRENT+self.numberofstocks
                        receiver_stock.TRENT=receiver_stock.TRENT-self.numberofstocks
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
    reporter=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reporter")
    reporting=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.reporter}"