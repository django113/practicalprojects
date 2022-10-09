from django.contrib import admin
from .models import CustomUser, DeliveryAddress


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'type', 'is_staff', 'date_joined']

    def save_model(self, request, obj, form, change):
        obj.set_password(obj.password)
        obj.save()
        super(CustomUser, self).save_model(request, obj, form, change)


@admin.register(DeliveryAddress)
class Delivery(admin.ModelAdmin):
    list_display = ['user', 'area', 'city', 'state', 'pincode']
