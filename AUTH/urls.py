from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='email_login'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh_token'),
    path('phone', views.PhoneAuthentication.as_view(), name='phone_login'),
    path('signup', views.NormalUserSignUpView.as_view(), name='new_user_signup'),
    path('otp/verify', views.VerifyOTP.as_view(), name='verify_otp')
]
