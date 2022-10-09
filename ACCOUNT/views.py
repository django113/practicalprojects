from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.exceptions import NotFound, PermissionDenied
from .serializers import DeliveryAddressSerializer, UserProfileUpdateSerializer, UserProfileSerializer
from .models import DeliveryAddress

User = get_user_model()


class ProfileUpdateView(RetrieveUpdateAPIView):
    """ User can update his profile information """

    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            user = User.objects.get(email=self.request.query_params.get('email'))
            self.check_object_permissions(self.request, user)
            return user

        except User.DoesNotExist:
            raise NotFound

    def check_object_permissions(self, request, obj):
        if not obj == request.user:
            raise PermissionDenied

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return UserProfileSerializer
        return UserProfileUpdateSerializer


class DeliveryAddressAll(ListAPIView):
    """ Return the list of all address added by user """

    permission_classes = [IsAuthenticated]
    serializer_class = DeliveryAddressSerializer

    def get_queryset(self):
        return DeliveryAddress.objects.filter(user=self.request.user)


class DeliveryAddressUpdateView(RetrieveUpdateAPIView):
    """ User can update his delivery address """

    permission_classes = [IsAuthenticated]
    serializer_class = DeliveryAddressSerializer

    def get_object(self):
        try:
            address = DeliveryAddress.objects.get(id=self.kwargs.get('id'))
            self.check_object_permissions(self.request, address)
            return address

        except DeliveryAddress.DoesNotExist:
            raise NotFound

    def check_object_permissions(self, request, obj):
        if not obj.user == request.user:
            raise PermissionDenied
