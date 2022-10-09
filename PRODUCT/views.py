from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ProductDetailSerializer, CategorySerializer, ProductSerializer
from .models import Product, Category
from .filter import ProductFilter


class CategoryListView(ListAPIView):
    """ All Category List """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductRetrieveView(RetrieveAPIView):
    """ Product Retrieve View """

    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_url_kwarg = "product"


class ProductListView(ListAPIView):
    """ All Product List View """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class SearchProductView(ListAPIView):
    """ Return the search result """

    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    queryset = Product.objects.all()
