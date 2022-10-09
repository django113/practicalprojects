from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class StaffMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['last_login', 'is_superuser', 'date_joined', 'groups', 'user_permissions']

    def create(self, validated_data):
        user = super(StaffMemberSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
