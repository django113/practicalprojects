from django.urls import path
from . import views

urlpatterns = [
    path('orders', views.AllOrderListView.as_view(), name='order_list'),
    path('order/assign', views.AssignOrderView.as_view(), name='assign_order')
]
