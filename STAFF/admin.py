from django.contrib import admin
from .models import DeliveryUser


@admin.register(DeliveryUser)
class DeliveryUser(admin.ModelAdmin):
    list_display = ['user', 'city', 'vehicle_number', 'verified']
