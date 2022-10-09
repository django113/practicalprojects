import re
import pyotp
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, authenticate
from datetime import datetime
from django.utils.timezone import make_aware
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSignUpSerializer

User = get_user_model()


class NormalUserSignUpView(CreateAPIView):
    """ The signup API for a normal user """

    serializer_class = UserSignUpSerializer
    queryset = User.objects.all()


class PhoneAuthentication(APIView):
    """ This API allow to use OTP based authentication """

    def generate_otp(self, user):
        time = datetime.now()
        user.last_otp = make_aware(time)
        user.save()
        otp = pyotp.TOTP(str(user.key))
        return otp.at(for_time=user.last_otp, counter_offset=1)
        # send the otp to user by sms here

    def post(self, request, *args, **kwargs):
        number = request.query_params.get('phone', '')

        if self.validate_number(number):
            user = authenticate(phone=number)

            if user is not None:
                otp = self.generate_otp(user)
                return Response(data={'phone': user.phone, 'otp': otp, 'message': 'otp send successfully'})

        return Response(data={'error': "invalid phone number"}, status=status.HTTP_406_NOT_ACCEPTABLE)

    # validate the Indian phone number
    def validate_number(self, number):
        if re.match("^[6-9]\d{9}$", number):
            return True
        return False


class VerifyOTP(APIView):
    """ Verify Your OTP """

    def post(self, request, *args, **kwargs):
        phone = request.query_params.get('phone', None)
        code = request.query_params.get('otp', None)

        if code is not None and phone is not None:
            user = authenticate(phone=phone)

            if user:
                otp = pyotp.TOTP(str(user.key))
                if otp.verify(otp=code, for_time=user.last_otp, valid_window=1):
                    token = RefreshToken.for_user(user)
                    return Response({'phone': user.phone, 'token': str(token.access_token), 'verified': 'true'})

        return Response({'phone': phone, 'verified': 'false'})
