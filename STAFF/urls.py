from django.urls import path
from . import views

urlpatterns = [
    path('product/category/add', views.AddCategoryView.as_view(), name='add_category'),
    path('product/category/modify/<str:id>', views.RetrieveUpdateDeleteCategoryView.as_view(), name='edit_category'),
    path('product/add', views.AddProductView.as_view(), name='add_product'),
    path('product/modify/<str:product>', views.ProductUpdateDeleteView.as_view(), name='product_update_delete'),
    path('register/delivery-executive', views.RegisterDeliveryUserView.as_view(), name='add_delivery_user'),
    path('edit/delivery-executive/<str:email>', views.UpdateDeliveryUserView.as_view(), name='delivery_user_info_update')
]
