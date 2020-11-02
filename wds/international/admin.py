from django.contrib import admin
from .models import trade,Stock,tradereq,Report,StockList
# Register your models here.
class stockadmin(admin.ModelAdmin):
    list_display=('user','userbalance','TM','UL','CVX','BRK','JPM','T','WFC','HD','KO','VISA','WMT','AXP','BA','PFE','VZ','HMC','QCOM','NFLX','FB','ADBE','VWS','GAZP','GS','MCD','ZM','PYPL','TCEHY','BABA','AAPL','MSFT','TSLA','TXN','INTC')

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