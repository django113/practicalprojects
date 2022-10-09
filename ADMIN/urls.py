from django.urls import path
from . import views

urlpatterns = [
    path('staff/add', views.CreateStaffMember.as_view(), name='add_staff_member')
]
