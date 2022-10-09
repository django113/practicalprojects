from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class PasswordLessAuthBackend(ModelBackend):
    """ User can login through OTP verification no need of password """

    def authenticate(self, request, phone=None, password=None, **kwargs):
        try:
            return User.objects.get(phone=phone)

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)

        except User.DoesNotExist:
            return None
