from rest_framework import serializers
from PRODUCT.serializers import OrderProductSerializer
from .models import Order, OrderDetails


class OrderDetailSerializer(serializers.ModelSerializer):
    product = OrderProductSerializer(many=True)
    order_address = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'user', 'amount', 'order_address', 'product')

    def get_order_address(self, obj):
        return str(obj.address)

    def to_representation(self, instance):
        data = super(OrderDetailSerializer, self).to_representation(instance)

        for product in data['product']:
            product.update({'quantity': OrderDetails.objects.get(order=instance, product_id=product['id']).quantity})

        return data


class OrderLessDetailSerializer(serializers.ModelSerializer):
    order_address = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_address']

    def get_order_address(self, obj):
        return str(obj.address)

    def get_user(self, obj):
        print(obj)
        return str(obj.user.name)
