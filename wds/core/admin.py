from django.contrib import admin
from .models import trade,Stock,tradereq,Report
# Register your models here.
class stockadmin(admin.ModelAdmin):
    list_display=('user','stock1','stock2','stock3','stock4','stock5','stock6','stock7','stock8','stock9','stock10','userbalance')

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
