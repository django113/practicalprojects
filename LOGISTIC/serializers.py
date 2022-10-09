from rest_framework import serializers
from rest_framework.exceptions import APIException
from LOGISTIC.models import AssignedOrder
from ORDER.models import Order


class OrderLogisticSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'phone', 'address', 'amount']

    def get_user(self, obj):
        return obj.user.name

    def get_address(self, obj):
        return str(obj.address)

    def get_phone(self, obj):
        return str(obj.user.phone)


class AssignOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedOrder
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data['delivery_executive']
        if user.type != 'delivery':
            raise APIException("invalid user selected")

        orders = validated_data['orders']

        for order in orders:
            order.delivery_status = 'out for delivery'
            order.save()

        return super(AssignOrderSerializer, self).create(validated_data)
