from django.db import models
from django.conf import settings
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
)

class Stock(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    stock1=models.IntegerField(default=0)
    stock1=models.IntegerField(default=0)

class trade(models.Model):
    seller=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stock=models.CharField(choices=stock_list,max_length=100)
    numberofstocks=models.IntegerField(default=0)
    priceperstock=models.FloatField(null=True, blank=True)
    buyer=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='buyer_of_stock', on_delete=models.CASCADE)
    userbalance=models.FloatField(default=1000000.0)