from django.contrib import admin
from .models import Order, OrderDetails


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'status', 'datetimestamp', 'address']


@admin.register(OrderDetails)
class OrderDetail(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity']
