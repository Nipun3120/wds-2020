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
    ('TM','TM'),
    ('UL','UL'),
    ('CVX','CVX'),
    ('BRK','BRK'),
    ('JPM','JPM'),
    ('T','T'),
    ('WFC','WFC'),
    ('HD','HD'),
    ('KO','KO'),
    ('VISA','VISA'),
    ('WMT','WMT'),
    ('AXP','AXP'),
    ('BA','BA'),
    ('PFE','PFE'),
    ('VZ','VZ'),
    ('HMC','HMC'),
    ('QCOM','QCOM'),
    ('NFLX','NFLX'),
    ('FB','FB'),
    ('ADBE','ADBE'),
    ('VWS','VWS'),
    ('GAZP','GAZP'),
    ('GS','GS'),
    ('MCD','MCD'),
    ('ZM','ZM'),
    ('PYPL','PYPL'),
    ('TCECHY','TCECHY'),
    ('BABA','BABA'),
    ('AAPL','AAPL'),
    ('MSFT','MSFT'),
    ('TSLA','TSLA'),
    ('TXN','TXN'),
    ('INTC','INTC'),
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
    userbalance=models.FloatField(default=1000000.0)
    TM=models.IntegerField(default=0)
    UL=models.IntegerField(default=0)
    CVX=models.IntegerField(default=0)
    BRK=models.IntegerField(default=0)
    JPM=models.IntegerField(default=0)
    T=models.IntegerField(default=0)
    WFC=models.IntegerField(default=0)
    HD=models.IntegerField(default=0)
    KO=models.IntegerField(default=0)
    VISA=models.IntegerField(default=0)
    WMT=models.IntegerField(default=0)
    AXP=models.IntegerField(default=0)
    BA=models.IntegerField(default=0)
    PFE=models.IntegerField(default=0)
    VZ=models.IntegerField(default=0)
    HMC=models.IntegerField(default=0)
    QCOM=models.IntegerField(default=0)
    NFLX=models.IntegerField(default=0)
    FB=models.IntegerField(default=0)
    ADBE=models.IntegerField(default=0)
    VWS=models.IntegerField(default=0)
    GAZP=models.IntegerField(default=0)
    GS=models.IntegerField(default=0)
    MCD=models.IntegerField(default=0)
    ZM=models.IntegerField(default=0)
    PYPL=models.IntegerField(default=0)
    TCEHY=models.IntegerField(default=0)
    BABA=models.IntegerField(default=0)
    AAPL=models.IntegerField(default=0)
    MSFT=models.IntegerField(default=0)
    TSLA=models.IntegerField(default=0)
    TXN=models.IntegerField(default=0)
    INTC=models.IntegerField(default=0)
    
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
            if self.stock=='TM':
                if (receiver_stock.TM>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.TM=sender_stock.TM+self.numberofstocks
                        receiver_stock.TM=receiver_stock.TM-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='UL':
                if (receiver_stock.UL>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.UL=sender_stock.UL+self.numberofstocks
                        receiver_stock.UL=receiver_stock.UL-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='CVX':
                if (receiver_stock.CVX>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.CVX=sender_stock.CVX+self.numberofstocks
                        receiver_stock.CVX=receiver_stock.CVX-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='BRK':
                if (receiver_stock.BRK>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.BRK=sender_stock.BRK+self.numberofstocks
                        receiver_stock.BRK=receiver_stock.BRK-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='JPM':
                if (receiver_stock.JPM>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.TM=sender_stock.JPM+self.numberofstocks
                        receiver_stock.JPM=receiver_stock.JPM-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='T':
                if (receiver_stock.T>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.T=sender_stock.T+self.numberofstocks
                        receiver_stock.T=receiver_stock.T-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='WFC':
                if (receiver_stock.WFC>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.WFC=sender_stock.WFC+self.numberofstocks
                        receiver_stock.WFC=receiver_stock.WFC-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='HD':
                if (receiver_stock.HD>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.HD=sender_stock.HD+self.numberofstocks
                        receiver_stock.HD=receiver_stock.HD-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='KO':
                if (receiver_stock.KO>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.KO=sender_stock.KO+self.numberofstocks
                        receiver_stock.KO=receiver_stock.KO-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='VISA':
                if (receiver_stock.VISA>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.VISA=sender_stock.VISA+self.numberofstocks
                        receiver_stock.VISA=receiver_stock.VISA-self.numberofstocks
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
            elif self.stock=='AXP':
                if (receiver_stock.AXP>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.AXP=sender_stock.AXP+self.numberofstocks
                        receiver_stock.AXP=receiver_stock.AXP-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='BA':
                if (receiver_stock.BA>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.BA=sender_stock.BA+self.numberofstocks
                        receiver_stock.BA=receiver_stock.BA-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='PFE':
                if (receiver_stock.PFE>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.PFE=sender_stock.PFE+self.numberofstocks
                        receiver_stock.PFE=receiver_stock.PFE-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='VZ':
                if (receiver_stock.VZ>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.VZ=sender_stock.VZ+self.numberofstocks
                        receiver_stock.VZ=receiver_stock.VZ-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='HMC':
                if (receiver_stock.HMC>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.HMC=sender_stock.HMC+self.numberofstocks
                        receiver_stock.HMC=receiver_stock.HMC-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='QCOM':
                if (receiver_stock.QCOM>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.QCOM=sender_stock.QCOM+self.numberofstocks
                        receiver_stock.QCOM=receiver_stock.QCOM-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='NFLX':
                if (receiver_stock.NFLX>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.NFLX=sender_stock.NFLX+self.numberofstocks
                        receiver_stock.NFLX=receiver_stock.NFLX-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='FB':
                if (receiver_stock.FB>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.FB=sender_stock.FB+self.numberofstocks
                        receiver_stock.FB=receiver_stock.FB-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='ADBE':
                if (receiver_stock.ADBE>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.ADBE=sender_stock.ADBE+self.numberofstocks
                        receiver_stock.ADBE=receiver_stock.ADBE-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='VWS':
                if (receiver_stock.VWS>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.VWS=sender_stock.VWS+self.numberofstocks
                        receiver_stock.VWS=receiver_stock.VWS-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='GAZP':
                if (receiver_stock.GAZP>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.GAZP=sender_stock.GAZP+self.numberofstocks
                        receiver_stock.GAZP=receiver_stock.GAZP-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='GS':
                if (receiver_stock.GS>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.GS=sender_stock.GS+self.numberofstocks
                        receiver_stock.GS=receiver_stock.GS-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='MCD':
                if (receiver_stock.MCD>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.MCD=sender_stock.MCD+self.numberofstocks
                        receiver_stock.MCD=receiver_stock.MCD-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='ZM':
                if (receiver_stock.ZM>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.ZM=sender_stock.ZM+self.numberofstocks
                        receiver_stock.ZM=receiver_stock.ZM-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='PYPL':
                if (receiver_stock.PYPL>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.PYPL=sender_stock.PYPL+self.numberofstocks
                        receiver_stock.PYPL=receiver_stock.PYPL-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='TCEHY':
                if (receiver_stock.TCEHY>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.TCEHY=sender_stock.TCEHY+self.numberofstocks
                        receiver_stock.TCEHY=receiver_stock.TCEHY-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='BABA':
                if (receiver_stock.BABA>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.BABA=sender_stock.BABA+self.numberofstocks
                        receiver_stock.BABA=receiver_stock.BABA-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='AAPL':
                if (receiver_stock.AAPL>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.AAPL=sender_stock.AAPL+self.numberofstocks
                        receiver_stock.AAPL=receiver_stock.AAPL-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='MSFT':
                if (receiver_stock.MSFT>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.MSFT=sender_stock.MSFT+self.numberofstocks
                        receiver_stock.MSFT=receiver_stock.MSFT-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='TSLA':
                if (receiver_stock.TSLA>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.TSLA=sender_stock.TSLA+self.numberofstocks
                        receiver_stock.TSLA=receiver_stock.TSLA-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='TXN':
                if (receiver_stock.TXN>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.TXN=sender_stock.TXN+self.numberofstocks
                        receiver_stock.TXN=receiver_stock.TXN-self.numberofstocks
                        self.is_active=False
                        self.status='accepted'
                    else:
                        return ('Currently Sender have Insufficient Balance to Buy!')
                else:
                    return ('Insufficient Stock Holdings')
            elif self.stock=='INTC':
                if (receiver_stock.INTC>=self.numberofstocks):
                    if(sender_stock.userbalance>=amount):
                        sender_stock.INTC=sender_stock.INTC+self.numberofstocks
                        receiver_stock.INTC=receiver_stock.INTC-self.numberofstocks
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
                if self.stock=='TM':
                    if(sender_stock.TM>=self.numberofstocks):
                        sender_stock.TM=sender_stock.TM+self.numberofstocks
                        receiver_stock.TM=receiver_stock.TM-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='UL':
                    if(sender_stock.UL>=self.numberofstocks):
                        sender_stock.UL=sender_stock.UL+self.numberofstocks
                        receiver_stock.UL=receiver_stock.UL-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='CVX':
                    if(sender_stock.CVX>=self.numberofstocks):
                        sender_stock.CVX=sender_stock.CVX+self.numberofstocks
                        receiver_stock.CVX=receiver_stock.CVX-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='BRK':
                    if(sender_stock.BRK>=self.numberofstocks):
                        sender_stock.BRK=sender_stock.BRK+self.numberofstocks
                        receiver_stock.BRK=receiver_stock.BRK-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='JPM':
                    if(sender_stock.JPM>=self.numberofstocks):
                        sender_stock.JPM=sender_stock.JPM+self.numberofstocks
                        receiver_stock.JPM=receiver_stock.JPM-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='T':
                    if(sender_stock.T>=self.numberofstocks):
                        sender_stock.T=sender_stock.T+self.numberofstocks
                        receiver_stock.T=receiver_stock.T-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='WFC':
                    if(sender_stock.WFC>=self.numberofstocks):
                        sender_stock.WFC=sender_stock.WFC+self.numberofstocks
                        receiver_stock.WFC=receiver_stock.WFC-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='HD':
                    if(sender_stock.HD>=self.numberofstocks):
                        sender_stock.HD=sender_stock.HD+self.numberofstocks
                        receiver_stock.HD=receiver_stock.HD-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='KO':
                    if(sender_stock.KO>=self.numberofstocks):
                        sender_stock.KO=sender_stock.KO+self.numberofstocks
                        receiver_stock.KO=receiver_stock.KO-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='VISA':
                    if(sender_stock.VISA>=self.numberofstocks):
                        sender_stock.VISA=sender_stock.VISA+self.numberofstocks
                        receiver_stock.VISA=receiver_stock.VISA-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='WMT':
                    if(sender_stock.WMT>=self.numberofstocks):
                        sender_stock.WMT=sender_stock.WMT+self.numberofstocks
                        receiver_stock.WMT=receiver_stock.WMT-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='AXP':
                    if(sender_stock.AXP>=self.numberofstocks):
                        sender_stock.AXP=sender_stock.AXP+self.numberofstocks
                        receiver_stock.AXP=receiver_stock.AXP-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='BA':
                    if(sender_stock.BA>=self.numberofstocks):
                        sender_stock.BA=sender_stock.BA+self.numberofstocks
                        receiver_stock.BA=receiver_stock.BA-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='PFE':
                    if(sender_stock.PFE>=self.numberofstocks):
                        sender_stock.PFE=sender_stock.PFE+self.numberofstocks
                        receiver_stock.PFE=receiver_stock.PFE-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='VZ':
                    if(sender_stock.VZ>=self.numberofstocks):
                        sender_stock.VZ=sender_stock.VZ+self.numberofstocks
                        receiver_stock.VZ=receiver_stock.VZ-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='HMC':
                    if(sender_stock.HMC>=self.numberofstocks):
                        sender_stock.HMC=sender_stock.HMC+self.numberofstocks
                        receiver_stock.HMC=receiver_stock.HMC-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='QCOM':
                    if(sender_stock.QCOM>=self.numberofstocks):
                        sender_stock.QCOM=sender_stock.QCOM+self.numberofstocks
                        receiver_stock.QCOM=receiver_stock.QCOM-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='NFLX':
                    if(sender_stock.NFLX>=self.numberofstocks):
                        sender_stock.NFLX=sender_stock.NFLX+self.numberofstocks
                        receiver_stock.NFLX=receiver_stock.NFLX-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='FB':
                    if(sender_stock.FB>=self.numberofstocks):
                        sender_stock.FB=sender_stock.FB+self.numberofstocks
                        receiver_stock.FB=receiver_stock.FB-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='ADBE':
                    if(sender_stock.ADBE>=self.numberofstocks):
                        sender_stock.ADBE=sender_stock.ADBE+self.numberofstocks
                        receiver_stock.ADBE=receiver_stock.ADBE-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='VWS':
                    if(sender_stock.VWS>=self.numberofstocks):
                        sender_stock.VWS=sender_stock.VWS+self.numberofstocks
                        receiver_stock.VWS=receiver_stock.VWS-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='GAZP':
                    if(sender_stock.GAZP>=self.numberofstocks):
                        sender_stock.GAZP=sender_stock.GAZP+self.numberofstocks
                        receiver_stock.GAZP=receiver_stock.GAZP-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='GS':
                    if(sender_stock.GS>=self.numberofstocks):
                        sender_stock.GS=sender_stock.GS+self.numberofstocks
                        receiver_stock.GS=receiver_stock.GS-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='MCD':
                    if(sender_stock.MCD>=self.numberofstocks):
                        sender_stock.MCD=sender_stock.MCD+self.numberofstocks
                        receiver_stock.MCD=receiver_stock.MCD-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='ZM':
                    if(sender_stock.ZM>=self.numberofstocks):
                        sender_stock.ZM=sender_stock.ZM+self.numberofstocks
                        receiver_stock.ZM=receiver_stock.ZM-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='PYPL':
                    if(sender_stock.PYPL>=self.numberofstocks):
                        sender_stock.PYPL=sender_stock.PYPL+self.numberofstocks
                        receiver_stock.PYPL=receiver_stock.PYPL-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='TCEHY':
                    if(sender_stock.TCEHY>=self.numberofstocks):
                        sender_stock.TCEHY=sender_stock.TCEHY+self.numberofstocks
                        receiver_stock.TCEHY=receiver_stock.TCEHY-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='BABA':
                    if(sender_stock.BABA>=self.numberofstocks):
                        sender_stock.BABA=sender_stock.BABA+self.numberofstocks
                        receiver_stock.BABA=receiver_stock.BABA-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='AAPL':
                    if(sender_stock.AAPL>=self.numberofstocks):
                        sender_stock.AAPL=sender_stock.AAPL+self.numberofstocks
                        receiver_stock.AAPL=receiver_stock.AAPL-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='MSFT':
                    if(sender_stock.MSFT>=self.numberofstocks):
                        sender_stock.MSFT=sender_stock.MSFT+self.numberofstocks
                        receiver_stock.MSFT=receiver_stock.MSFT-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='TSLA':
                    if(sender_stock.TSLA>=self.numberofstocks):
                        sender_stock.TSLA=sender_stock.TSLA+self.numberofstocks
                        receiver_stock.TSLA=receiver_stock.TSLA-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='TXN':
                    if(sender_stock.TXN>=self.numberofstocks):
                        sender_stock.TXN=sender_stock.TXN+self.numberofstocks
                        receiver_stock.TXN=receiver_stock.TXN-self.numberofstocks
                    else:
                        return ('Currently Sender do not have sufficient stocks to sell!')
                elif self.stock=='INTC':
                    if(sender_stock.INTC>=self.numberofstocks):
                        sender_stock.INTC=sender_stock.INTC+self.numberofstocks
                        receiver_stock.INTC=receiver_stock.INTC-self.numberofstocks
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