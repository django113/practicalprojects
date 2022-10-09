from django.urls import path
from . import views

urlpatterns = [
    path('attendance', views.MarkAttendanceView.as_view(), name='add_attendance'),
    path('orders', views.DeliveryOrderView.as_view(), name='delivery_orders'),
]
