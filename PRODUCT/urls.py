from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.CategoryListView.as_view(), name='category_list'),
    path('view', views.ProductListView.as_view(), name='all_product_list'),
    path('search', views.SearchProductView.as_view(), name='search_product'),
    path('view/<str:product>', views.ProductRetrieveView.as_view(), name='product_view')
]
