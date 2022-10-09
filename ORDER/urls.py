from django.urls import path
from . import views

urlpatterns = [
    path('new', views.CreateOrderView.as_view(), name='new_order'),
    path('history', views.UserOrderListView.as_view(), name='order_history'),
    path('details/<str:id>', views.UserOrderDetailView.as_view(), name='order_details')
]
