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
    ('JPM','JPM'),
    ('ATT','ATT'),
    ('CCA','CCA'),
    ('WMT','WMT'),
    ('AER','AER'),
    ('BOE','BOE'),
    ('PFZ','PFZ'),
    ('FBI','FBI'),
    ('ZVC','ZVC'),
    ('PAP','PAP'),
    ('TXT','TXT'),
    ('GMS','GMS'),
    ('APL','APL'),
    ('TES','TES'),
    ('INT','INT'),
    
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
    userbalance=models.FloatField(default=100000.0)
    JPM=models.IntegerField(default=0)
    ATT=models.IntegerField(default=0)
    CCA=models.IntegerField(default=0)
    WMT=models.IntegerField(default=0)
    AER=models.IntegerField(default=0)
    BOE=models.IntegerField(default=0)
    PFZ=models.IntegerField(default=0)
    FBI=models.IntegerField(default=0)
    ZVC=models.IntegerField(default=0)
    PAP=models.IntegerField(default=0)
    TXT=models.IntegerField(default=0)
    GMS=models.IntegerField(default=0)
    APL=models.IntegerField(default=0)
    TES=models.IntegerField(default=0)
    INT=models.IntegerField(default=0)
    
    
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
            if self.stock=='JPM':
                if (receiver_stock.JPM>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.JPM=sender_stock.JPM+self.numberofstocks
                        receiver_stock.JPM=receiver_stock.JPM-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='ATT':
                if (receiver_stock.ATT>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.ATT=sender_stock.ATT+self.numberofstocks
                        receiver_stock.ATT=receiver_stock.ATT-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='CCA':
                if (receiver_stock.CCA>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.CCA=sender_stock.CCA+self.numberofstocks
                        receiver_stock.CCA=receiver_stock.CCA-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='WMT':
                if (receiver_stock.WMT>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.WMT=sender_stock.WMT+self.numberofstocks
                        receiver_stock.WMT=receiver_stock.WMT-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            
            elif self.stock=='AER':
                if (receiver_stock.AER>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.AER=sender_stock.AER+self.numberofstocks
                        receiver_stock.AER=receiver_stock.AER-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='BOE':
                if (receiver_stock.BOE>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.BOE=sender_stock.BOE+self.numberofstocks
                        receiver_stock.BOE=receiver_stock.BOE-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='PFZ':
                if (receiver_stock.PFZ>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.PFZ=sender_stock.PFZ+self.numberofstocks
                        receiver_stock.PFZ=receiver_stock.PFZ-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='FBI':
                if (receiver_stock.FBI>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.FBI=sender_stock.FBI+self.numberofstocks
                        receiver_stock.FBI=receiver_stock.FBI-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            
            elif self.stock=='ZVC':
                if (receiver_stock.ZVC>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.ZVC=sender_stock.ZVC+self.numberofstocks
                        receiver_stock.ZVC=receiver_stock.ZVC-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='PAP':
                if (receiver_stock.PAP>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.PAP=sender_stock.PAP+self.numberofstocks
                        receiver_stock.PAP=receiver_stock.PAP-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='TXT':
                if (receiver_stock.TXT>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.TXT=sender_stock.TXT+self.numberofstocks
                        receiver_stock.TXT=receiver_stock.TXT-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='GMS':
                if (receiver_stock.GMS>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.GMS=sender_stock.GMS+self.numberofstocks
                        receiver_stock.GMS=receiver_stock.GMS-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='APL':
                if (receiver_stock.APL>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.APL=sender_stock.APL+self.numberofstocks
                        receiver_stock.APL=receiver_stock.APL-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='TES':
                if (receiver_stock.TES>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.TES=sender_stock.TES+self.numberofstocks
                        receiver_stock.TES=receiver_stock.TES-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='INT':
                if (receiver_stock.INT>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.INT=sender_stock.INT+self.numberofstocks
                        receiver_stock.INT=receiver_stock.INT-self.numberofstocks
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
            if (amount<=sender_stock.userbalance):
                
                sender_stock.userbalance=sender_stock.userbalance-amount
                receiver_stock.userbalance=receiver_stock.userbalance+amount
                if self.stock=='JPM':
                    if(receiver_stock.JPM>=self.numberofstocks):
                        sender_stock.JPM=sender_stock.JPM+self.numberofstocks
                        receiver_stock.JPM=receiver_stock.JPM-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='ATT':
                    if(receiver_stock.ATT>=self.numberofstocks):
                        sender_stock.ATT=sender_stock.ATT+self.numberofstocks
                        receiver_stock.ATT=receiver_stock.ATT-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='CCA':
                    if(receiver_stock.CCA>=self.numberofstocks):
                        sender_stock.CCA=sender_stock.CCA+self.numberofstocks
                        receiver_stock.CCA=receiver_stock.CCA-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='WMT':
                    if(receiver_stock.WMT>=self.numberofstocks):
                        sender_stock.WMT=sender_stock.WMT+self.numberofstocks
                        receiver_stock.WMT=receiver_stock.WMT-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='AER':
                    if(receiver_stock.AER>=self.numberofstocks):
                        sender_stock.AER=sender_stock.AER+self.numberofstocks
                        receiver_stock.AER=receiver_stock.AER-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='BOE':
                    if(receiver_stock.BOE>=self.numberofstocks):
                        sender_stock.BOE=sender_stock.BOE+self.numberofstocks
                        receiver_stock.BOE=receiver_stock.BOE-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='PFZ':
                    if(receiver_stock.PFZ>=self.numberofstocks):
                        sender_stock.PFZ=sender_stock.PFZ+self.numberofstocks
                        receiver_stock.PFZ=receiver_stock.PFZ-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='FBI':
                    if(receiver_stock.FBI>=self.numberofstocks):
                        sender_stock.FBI=sender_stock.FBI+self.numberofstocks
                        receiver_stock.FBI=receiver_stock.FBI-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='ZVC':
                    if(receiver_stock.ZVC>=self.numberofstocks):
                        sender_stock.ZVC=sender_stock.ZVC+self.numberofstocks
                        receiver_stock.ZVC=receiver_stock.ZVC-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='PAP':
                    if(receiver_stock.PAP>=self.numberofstocks):
                        sender_stock.PAP=sender_stock.PAP+self.numberofstocks
                        receiver_stock.PAP=receiver_stock.PAP-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='TXT':
                    if(receiver_stock.TXT>=self.numberofstocks):
                        sender_stock.TXT=sender_stock.TXT+self.numberofstocks
                        receiver_stock.TXT=receiver_stock.TXT-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='GMS':
                    if(receiver_stock.GMS>=self.numberofstocks):
                        sender_stock.GMS=sender_stock.GMS+self.numberofstocks
                        receiver_stock.GMS=receiver_stock.GMS-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='APL':
                    if(receiver_stock.APL>=self.numberofstocks):
                        sender_stock.APL=sender_stock.APL+self.numberofstocks
                        receiver_stock.APL=receiver_stock.APL-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='TES':
                    if(receiver_stock.TES>=self.numberofstocks):
                        sender_stock.TES=sender_stock.TES+self.numberofstocks
                        receiver_stock.TES=receiver_stock.TES-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='INT':
                    if(receiver_stock.INT>=self.numberofstocks):
                        sender_stock.INT=sender_stock.INT+self.numberofstocks
                        receiver_stock.INT=receiver_stock.INT-self.numberofstocks
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