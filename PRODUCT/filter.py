from django_filters import rest_framework as rest_filter
from .models import Product


class ProductFilter(rest_filter.FilterSet):
    name = rest_filter.CharFilter(field_name='name', lookup_expr='icontains')
    category = rest_filter.CharFilter(field_name='category__category', lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['name']
