from django.contrib import admin
from .models import trade,Stock,tradereq,Report,StockList
# Register your models here.
class stockadmin(admin.ModelAdmin):
    list_display=('user','ASHOKLEY','WIPRO','RAJESHEXPO','AMBUJACEM','MM','ONGC','DMART','SUNPHARMA','stock9','ADANIPOWER','userbalance')

class tradeadmin(admin.ModelAdmin):
    list_display=('seller','stock','numberofstocks','priceperstock','buyer')
admin.site.register(Stock,stockadmin)
admin.site.register(trade,tradeadmin)

class requestadmin(admin.ModelAdmin):
    list_display=('sender','receiver','action')
admin.site.register(tradereq,requestadmin)

class reportadmin(admin.ModelAdmin):
    list_display=('reporter','reporting')
admin.site.register(Report,reportadmin)

class stocklistadmin(admin.ModelAdmin):
    list_display=('stockattribute','stockname','stockprice')
admin.site.register(StockList,stocklistadmin)