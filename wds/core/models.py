from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
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


class traderequest(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name ="receiver")
    is_active = models.BooleanField(blank=True, null=True, default=True)

    def __str__(self):
        return self.sender

    

