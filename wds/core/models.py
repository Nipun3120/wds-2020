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
    ('stock1','stock1'),
    ('stock2','stock2'),
    ('stock3','stock3'),
    ('stock4','stock4'),
    ('stock5','stock5'),
    ('stock6','stock6'),
    ('stock7','stock7'),
    ('stock8','stock8'),
    ('stock9','stock9'),
    ('stock10','stock10'),
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

class Stock(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    stock1=models.IntegerField(default=0)
    stock2=models.IntegerField(default=0)
    stock3=models.IntegerField(default=0)
    stock4=models.IntegerField(default=0)
    stock5=models.IntegerField(default=0)
    stock6=models.IntegerField(default=0)
    stock7=models.IntegerField(default=0)
    stock8=models.IntegerField(default=0)
    stock9=models.IntegerField(default=0)
    stock10=models.IntegerField(default=0)
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
            if self.stock=='stock1':
                sender_stock.stock1=sender_stock.stock1+self.numberofstocks
                receiver_stock.stock1=receiver_stock.stock1-self.numberofstocks
            elif self.stock=='stock2':
                sender_stock.stock2=sender_stock.stock2+self.numberofstocks
                receiver_stock.stock2=receiver_stock.stock2-self.numberofstocks
            elif self.stock=='stock3':
                sender_stock.stock3=sender_stock.stock3+self.numberofstocks
                receiver_stock.stock3=receiver_stock.stock3-self.numberofstocks
            elif self.stock=='stock4':
                sender_stock.stock4=sender_stock.stock4+self.numberofstocks
                receiver_stock.stock4=receiver_stock.stock4-self.numberofstocks
            elif self.stock=='stock5':
                sender_stock.stock5=sender_stock.stock5+self.numberofstocks
                receiver_stock.stock5=receiver_stock.stock5-self.numberofstocks
            elif self.stock=='stock6':
                sender_stock.stock6=sender_stock.stock6+self.numberofstocks
                receiver_stock.stock6=receiver_stock.stock6-self.numberofstocks
            elif self.stock=='stock7':
                sender_stock.stock7=sender_stock.stock7+self.numberofstocks
                receiver_stock.stock7=receiver_stock.stock7-self.numberofstocks
            elif self.stock=='stock8':
                sender_stock.stock8=sender_stock.stock8+self.numberofstocks
                receiver_stock.stock8=receiver_stock.stock8-self.numberofstocks
            elif self.stock=='stock9':
                sender_stock.stock9=sender_stock.stock9+self.numberofstocks
                receiver_stock.stock9=receiver_stock.stock9-self.numberofstocks
            elif self.stock=='stock10':
                sender_stock.stock10=sender_stock.stock10+self.numberofstocks
                receiver_stock.stock10=receiver_stock.stock10-self.numberofstocks
            
            receiver_stock.save()
            sender_stock.save()
        elif self.action=='sell':
            sender_stock,receiver_stock=receiver_stock,sender_stock
            sender_stock.userbalance=sender_stock.userbalance-amount
            receiver_stock.userbalance=receiver_stock.userbalance+amount
            if self.stock=='stock1':
                sender_stock.stock1=sender_stock.stock1+self.numberofstocks
                receiver_stock.stock1=receiver_stock.stock1-self.numberofstocks
            elif self.stock=='stock2':
                sender_stock.stock2=sender_stock.stock2+self.numberofstocks
                receiver_stock.stock2=receiver_stock.stock2-self.numberofstocks
            elif self.stock=='stock3':
                sender_stock.stock3=sender_stock.stock3+self.numberofstocks
                receiver_stock.stock3=receiver_stock.stock3-self.numberofstocks
            elif self.stock=='stock4':
                sender_stock.stock4=sender_stock.stock4+self.numberofstocks
                receiver_stock.stock4=receiver_stock.stock4-self.numberofstocks
            elif self.stock=='stock5':
                sender_stock.stock5=sender_stock.stock5+self.numberofstocks
                receiver_stock.stock5=receiver_stock.stock5-self.numberofstocks
            elif self.stock=='stock6':
                sender_stock.stock6=sender_stock.stock6+self.numberofstocks
                receiver_stock.stock6=receiver_stock.stock6-self.numberofstocks
            elif self.stock=='stock7':
                sender_stock.stock7=sender_stock.stock7+self.numberofstocks
                receiver_stock.stock7=receiver_stock.stock7-self.numberofstocks
            elif self.stock=='stock8':
                sender_stock.stock8=sender_stock.stock8+self.numberofstocks
                receiver_stock.stock8=receiver_stock.stock8-self.numberofstocks
            elif self.stock=='stock9':
                sender_stock.stock9=sender_stock.stock9+self.numberofstocks
                receiver_stock.stock9=receiver_stock.stock9-self.numberofstocks
            elif self.stock=='stock10':
                sender_stock.stock10=sender_stock.stock10+self.numberofstocks
                receiver_stock.stock10=receiver_stock.stock10-self.numberofstocks
            
            receiver_stock.save()
            sender_stock.save()
        self.is_active=False
        self.status="accepted"
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