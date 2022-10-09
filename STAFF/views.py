from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import serializers
from rest_framework.permissions import exceptions as permission
from PRODUCT.models import Category, Product
from PRODUCT.serializers import CategorySerializer, ProductDetailSerializer
from .permissions import StaffPermission
from .serializers import DeliveryUserDetailSerializer, DeliveryUserDetailsSerializer
from .models import DeliveryUser


class RegisterDeliveryUserView(CreateAPIView):
    """ Create Delivery User """

    permission_classes = [StaffPermission]
    serializer_class = DeliveryUserDetailSerializer
    queryset = DeliveryUser.objects.all()


class UpdateDeliveryUserView(RetrieveUpdateDestroyAPIView):
    """ Staff can update the information of delivery executive """

    permission_classes = [StaffPermission]
    serializer_class = DeliveryUserDetailsSerializer

    def get_object(self):
        try:
            user = DeliveryUser.objects.get(user__email=self.kwargs.get('email'))
            return user
        except DeliveryUser.DoesNotExist as error:
            raise serializers.ValidationError({'message': error})


class AddCategoryView(CreateAPIView):
    """ Add New Category """

    permission_classes = [StaffPermission]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class RetrieveUpdateDeleteCategoryView(RetrieveUpdateDestroyAPIView):
    """ Retrieve Update Delete Category """

    permission_classes = [StaffPermission]
    serializer_class = CategorySerializer

    def get_object(self):
        try:
            return Category.objects.get(id=self.kwargs.get('id'))
        except Category.DoesNotExist as error:
            raise serializers.ValidationError({'error': error})


class AddProductView(CreateAPIView):
    """ Add new product """

    permission_classes = [StaffPermission]
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

    def get_serializer_context(self):
        context = super(AddProductView, self).get_serializer_context()
        context['request'] = self.request
        return context

    def check_permissions(self, request):
        if self.request.user.is_authenticated and self.request.user.is_staff and self.request.user.type == 'manager':
            pass
        else:
            raise permission.PermissionDenied


class ProductUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """ Product Update Delete View """

    permission_classes = [StaffPermission]
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_url_kwarg = "product"

    def get_serializer_context(self):
        context = super(ProductUpdateDeleteView, self).get_serializer_context()
        context['request'] = self.request
        return context
