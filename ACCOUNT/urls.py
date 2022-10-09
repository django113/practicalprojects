from django.urls import path
from . import views

urlpatterns = [
    path('profile/update', views.ProfileUpdateView.as_view(), name='update_profile'),
    path('address/all', views.DeliveryAddressAll.as_view(), name='all_delivery_address'),
    path('address/update/<str:id>', views.DeliveryAddressUpdateView.as_view(), name='update_delivery_address'),
]
