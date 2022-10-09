from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class Attendance(admin.ModelAdmin):
    list_display = ['user', 'login_datetime', 'working']
