from django.contrib import admin
from .models import trade,Stock
# Register your models here.
admin.site.register(Stock)
admin.site.register(trade)