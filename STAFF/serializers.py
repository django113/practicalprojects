from django.contrib.auth import get_user_model
from rest_framework import serializers
from ACCOUNT.serializers import DeliveryUserSerializer
from .models import DeliveryUser

User = get_user_model()


class DeliveryUserDetailSerializer(serializers.ModelSerializer):
    user = DeliveryUserSerializer()

    class Meta:
        model = DeliveryUser
        fields = ['user', 'city', 'vehicle_number']

    def create(self, validated_data):
        user = User.objects.create(**validated_data['user'])
        user.set_password(validated_data['user']['password'])
        user.type = 'delivery'
        user.is_staff = True
        user.save()
        instance = DeliveryUser.objects.create(
            user=user,
            city=validated_data['city'],
            vehicle_number=validated_data['vehicle_number']
        )
        return instance


class DeliveryUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryUser
        exclude = ['user']
