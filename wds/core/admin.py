from django.contrib import admin
from .models import trade,Stock,FriendList,FriendRequest,tradereq
# Register your models here.
class stockadmin(admin.ModelAdmin):
    list_display=('user','stock1','stock2','stock3','stock4','stock5','stock6','stock7','stock8','stock9','stock10','userbalance')

class tradeadmin(admin.ModelAdmin):
    list_display=('seller','stock','numberofstocks','priceperstock','buyer')
admin.site.register(Stock,stockadmin)
admin.site.register(trade,tradeadmin)


class FriendListAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user']
    search_fields = ['user']
    readonly_fields = ['user',]

    class Meta:
        model = FriendList


admin.site.register(FriendList, FriendListAdmin)

class FriendRequestAdmin(admin.ModelAdmin):
    list_filter = ['sender', 'receiver']
    list_display = ['sender', 'receiver',]
    search_fields = ['sender__username', 'receiver__username']

    class Meta:
        model = FriendRequest


admin.site.register(FriendRequest, FriendRequestAdmin)

class requestadmin(admin.ModelAdmin):
    list_display=('sender','receiver','action')
admin.site.register(tradereq,requestadmin)