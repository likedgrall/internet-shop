from django.contrib import admin
from Shop.models import *

# Register your models here.

@admin.register(Snickers)
class SnickersAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'raits', 'quantity', 'cost') # указываем названия полей как в модели
    # list_editable = ('name', 'raits', 'quantity', 'cost')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('adress', 'product')