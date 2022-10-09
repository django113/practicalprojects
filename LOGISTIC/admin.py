from django.contrib import admin
from .models import AssignedOrder


@admin.register(AssignedOrder)
class AssignedOrderAdmin(admin.ModelAdmin):
    list_display = ['delivery_executive', 'delivery_datetime', 'description']
