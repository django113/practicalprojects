from django.contrib.auth import get_user_model
from rest_framework import serializers
from ACCOUNT.models import DeliveryAddress
from ACCOUNT.serializers import DeliveryAddressSerializer

User = get_user_model()


class UserSignUpSerializer(serializers.ModelSerializer):
    """ serialize the user details """

    user_delivery_address = DeliveryAddressSerializer(many=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'password', 'user_delivery_address']

    def create(self, validated_data):
        addresses = validated_data.pop('user_delivery_address')
        user = super(UserSignUpSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()

        for address in addresses:
            DeliveryAddress.objects.create(user=user, **address)

        return user
