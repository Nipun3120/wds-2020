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
    ('stock9','stock9'),
    ('ADANIPOWER','ADANIPOWER'),
    ('stock11','stock11'),
    ('stock12','stock12'),
    ('stock13','stock13'),
    ('stock14','stock14'),
    ('stock15','stock15'),
    ('stock16','stock16'),
    ('stock17','stock17'),
    ('stock18','stock18'),
    ('stock19','stock19'),
    ('stock20','stock20'),
    ('stock21','stock21'),
    ('stock22','stock22'),
    ('stock23','stock23'),
    ('stock24','stock24'),
    ('stock25','stock25'),
    ('stock26','stock26'),
    ('stock27','stock27'),
    ('stock28','stock28'),
    ('stock29','stock29'),
    ('stock30','stock30'),
    ('stock31','stock31'),
    ('stock32','stock32'),
    ('stock33','stock33'),
    
    
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
    stock9=models.IntegerField(default=0)
    ADANIPOWER=models.IntegerField(default=0)
    stock12=models.IntegerField(default=0)
    stock12=models.IntegerField(default=0)
    stock13=models.IntegerField(default=0)
    stock14=models.IntegerField(default=0)
    stock15=models.IntegerField(default=0)
    stock16=models.IntegerField(default=0)
    stock17=models.IntegerField(default=0)
    stock18=models.IntegerField(default=0)
    stock19=models.IntegerField(default=0)
    stock20=models.IntegerField(default=0)
    stock21=models.IntegerField(default=0)
    stock22=models.IntegerField(default=0)
    stock23=models.IntegerField(default=0)
    stock24=models.IntegerField(default=0)
    stock25=models.IntegerField(default=0)
    stock26=models.IntegerField(default=0)
    stock27=models.IntegerField(default=0)
    stock28=models.IntegerField(default=0)
    stock29=models.IntegerField(default=0)
    stock30=models.IntegerField(default=0)
    stock31=models.IntegerField(default=0)
    stock32=models.IntegerField(default=0)
    stock33=models.IntegerField(default=0)
    
    
    
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
            elif self.stock=='stock11':
                if (receiver_stock.stock11>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock11=sender_stock.stock11+self.numberofstocks
                        receiver_stock.stock11=receiver_stock.stock11-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock12':
                if (receiver_stock.stock12>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock12=sender_stock.stock12+self.numberofstocks
                        receiver_stock.stock12=receiver_stock.stock12-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock13':
                if (receiver_stock.stock13>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock13=sender_stock.stock13+self.numberofstocks
                        receiver_stock.stock13=receiver_stock.stock13-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock14':
                if (receiver_stock.stock14>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock14=sender_stock.stock14+self.numberofstocks
                        receiver_stock.stock14=receiver_stock.stock14-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock15':
                if (receiver_stock.stock15>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock15=sender_stock.stock15+self.numberofstocks
                        receiver_stock.stock15=receiver_stock.stock15-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock16':
                if (receiver_stock.stock16>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock16=sender_stock.stock16+self.numberofstocks
                        receiver_stock.stock16=receiver_stock.stock16-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock17':
                if (receiver_stock.stock17>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock17=sender_stock.stock17+self.numberofstocks
                        receiver_stock.stock17=receiver_stock.stock17-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock18':
                if (receiver_stock.stock18>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock18=sender_stock.stock18+self.numberofstocks
                        receiver_stock.stock18=receiver_stock.stock18-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock19':
                if (receiver_stock.stock19>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock19=sender_stock.stock19+self.numberofstocks
                        receiver_stock.stock19=receiver_stock.stock19-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock20':
                if (receiver_stock.stock20>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock20=sender_stock.stock20+self.numberofstocks
                        receiver_stock.stock20=receiver_stock.stock20-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock21':
                if (receiver_stock.stock21>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock21=sender_stock.stock21+self.numberofstocks
                        receiver_stock.stock21=receiver_stock.stock21-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock22':
                if (receiver_stock.stock22>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock22=sender_stock.stock22+self.numberofstocks
                        receiver_stock.stock22=receiver_stock.stock22-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock23':
                if (receiver_stock.stock23>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock23=sender_stock.stock23+self.numberofstocks
                        receiver_stock.stock23=receiver_stock.stock23-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock24':
                if (receiver_stock.stock24>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock24=sender_stock.stock24+self.numberofstocks
                        receiver_stock.stock24=receiver_stock.stock24-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock25':
                if (receiver_stock.stock25>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock25=sender_stock.stock25+self.numberofstocks
                        receiver_stock.stock25=receiver_stock.stock25-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock26':
                if (receiver_stock.stock26>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock26=sender_stock.stock26+self.numberofstocks
                        receiver_stock.stock26=receiver_stock.stock26-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock27':
                if (receiver_stock.stock27>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock27=sender_stock.stock27+self.numberofstocks
                        receiver_stock.stock27=receiver_stock.stock27-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock28':
                if (receiver_stock.stock28>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock28=sender_stock.stock28+self.numberofstocks
                        receiver_stock.stock28=receiver_stock.stock28-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock29':
                if (receiver_stock.stock29>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock29=sender_stock.stock29+self.numberofstocks
                        receiver_stock.stock29=receiver_stock.stock29-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock30':
                if (receiver_stock.stock30>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock30=sender_stock.stock30+self.numberofstocks
                        receiver_stock.stock30=receiver_stock.stock30-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock31':
                if (receiver_stock.stock31>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock31=sender_stock.stock31+self.numberofstocks
                        receiver_stock.stock31=receiver_stock.stock31-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock32':
                if (receiver_stock.stock32>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock32=sender_stock.stock32+self.numberofstocks
                        receiver_stock.stock32=receiver_stock.stock32-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='stock33':
                if (receiver_stock.stock33>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.stock33=sender_stock.stock33+self.numberofstocks
                        receiver_stock.stock33=receiver_stock.stock33-self.numberofstocks
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
                elif self.stock=='stock11':
                    if(sender_stock.stock11>=self.numberofstocks):
                        sender_stock.stock11=sender_stock.stock11+self.numberofstocks
                        receiver_stock.stock11=receiver_stock.stock11-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock12':
                    if(sender_stock.stock12>=self.numberofstocks):
                        sender_stock.stock12=sender_stock.stock12+self.numberofstocks
                        receiver_stock.stock12=receiver_stock.stock12-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock13':
                    if(sender_stock.stock13>=self.numberofstocks):
                        sender_stock.stock13=sender_stock.stock13+self.numberofstocks
                        receiver_stock.stock13=receiver_stock.stock13-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock14':
                    if(sender_stock.stock14>=self.numberofstocks):
                        sender_stock.stock14=sender_stock.stock14+self.numberofstocks
                        receiver_stock.stock14=receiver_stock.stock14-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock15':
                    if(sender_stock.stock15>=self.numberofstocks):
                        sender_stock.stock15=sender_stock.stock15+self.numberofstocks
                        receiver_stock.stock15=receiver_stock.stock15-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock16':
                    if(sender_stock.stock16>=self.numberofstocks):
                        sender_stock.stock16=sender_stock.stock16+self.numberofstocks
                        receiver_stock.stock16=receiver_stock.stock16-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock17':
                    if(sender_stock.stock17>=self.numberofstocks):
                        sender_stock.stock17=sender_stock.stock17+self.numberofstocks
                        receiver_stock.stock17=receiver_stock.stock17-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock18':
                    if(sender_stock.stock18>=self.numberofstocks):
                        sender_stock.stock18=sender_stock.stock18+self.numberofstocks
                        receiver_stock.stock18=receiver_stock.stock18-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock19':
                    if(sender_stock.stock19>=self.numberofstocks):
                        sender_stock.stock19=sender_stock.stock19+self.numberofstocks
                        receiver_stock.stock19=receiver_stock.stock19-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock20':
                    if(sender_stock.stock20>=self.numberofstocks):
                        sender_stock.stock20=sender_stock.stock20+self.numberofstocks
                        receiver_stock.stock20=receiver_stock.stock20-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock21':
                    if(sender_stock.stock21>=self.numberofstocks):
                        sender_stock.stock21=sender_stock.stock21+self.numberofstocks
                        receiver_stock.stock21=receiver_stock.stock21-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock22':
                    if(sender_stock.stock22>=self.numberofstocks):
                        sender_stock.stock22=sender_stock.stock22+self.numberofstocks
                        receiver_stock.stock22=receiver_stock.stock22-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock23':
                    if(sender_stock.stock23>=self.numberofstocks):
                        sender_stock.stock23=sender_stock.stock23+self.numberofstocks
                        receiver_stock.stock23=receiver_stock.stock23-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock24':
                    if(sender_stock.stock24>=self.numberofstocks):
                        sender_stock.stock24=sender_stock.stock24+self.numberofstocks
                        receiver_stock.stock24=receiver_stock.stock24-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock25':
                    if(sender_stock.stock25>=self.numberofstocks):
                        sender_stock.stock25=sender_stock.stock25+self.numberofstocks
                        receiver_stock.stock25=receiver_stock.stock25-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock26':
                    if(sender_stock.stock26>=self.numberofstocks):
                        sender_stock.stock26=sender_stock.stock26+self.numberofstocks
                        receiver_stock.stock26=receiver_stock.stock26-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock27':
                    if(sender_stock.stock27>=self.numberofstocks):
                        sender_stock.stock27=sender_stock.stock27+self.numberofstocks
                        receiver_stock.stock27=receiver_stock.stock27-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock28':
                    if(sender_stock.stock28>=self.numberofstocks):
                        sender_stock.stock28=sender_stock.stock28+self.numberofstocks
                        receiver_stock.stock28=receiver_stock.stock28-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock29':
                    if(sender_stock.stock29>=self.numberofstocks):
                        sender_stock.stock29=sender_stock.stock29+self.numberofstocks
                        receiver_stock.stock29=receiver_stock.stock29-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock30':
                    if(sender_stock.stock30>=self.numberofstocks):
                        sender_stock.stock30=sender_stock.stock30+self.numberofstocks
                        receiver_stock.stock30=receiver_stock.stock30-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock31':
                    if(sender_stock.stock31>=self.numberofstocks):
                        sender_stock.stock31=sender_stock.stock31+self.numberofstocks
                        receiver_stock.stock31=receiver_stock.stock31-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock32':
                    if(sender_stock.stock32>=self.numberofstocks):
                        sender_stock.stock32=sender_stock.stock32+self.numberofstocks
                        receiver_stock.stock32=receiver_stock.stock32-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='stock33':
                    if(sender_stock.stock33>=self.numberofstocks):
                        sender_stock.stock33=sender_stock.stock33+self.numberofstocks
                        receiver_stock.stock33=receiver_stock.stock33-self.numberofstocks
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