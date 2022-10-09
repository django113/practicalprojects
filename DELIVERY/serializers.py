from datetime import datetime
from rest_framework import serializers
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    """ store and manage the record of attendance """

    class Meta:
        model = Attendance
        exclude = ['user']

    def create(self, validated_data):
        try:
            attendance = Attendance.objects.get(
                user=self.context['user'],
                login_datetime__day=datetime.today().day,
                login_datetime__month=datetime.today().month,
                login_datetime__year=datetime.today().year
            )

        except Attendance.DoesNotExist:
            validated_data['user'] = self.context['user']
            user = super(AttendanceSerializer, self).create(validated_data)
            return user

        message = {
            'message': 'you are already logged in',
            'working': attendance.working,
            'datetimestamp': attendance.login_datetime
        }
        raise serializers.ValidationError(message)
