from django.db import models

# Create your models here.
class Stock(models.Model):
    StockName = models.CharField(blank=True, max_length=100)
    CurrentPrice = models.FloatField(null=True,blank=True)
    def __str__(self):
        return self.StockName