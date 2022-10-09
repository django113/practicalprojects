from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import DeliveryAddress

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'phone']


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    """ serialize user profile details """

    class Meta:
        model = User
        fields = ['name']


class DeliveryUserSerializer(serializers.ModelSerializer):
    """ serialize delivery user details """

    class Meta:
        model = User
        exclude = ['last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions', 'type']


class DeliveryAddressSerializer(serializers.ModelSerializer):
    """ serialize delivery address details """

    class Meta:
        model = DeliveryAddress
        exclude = ['user']
