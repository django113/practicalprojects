from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from .serializers import StaffMemberSerializer
from .permissions import IsAdminPermission

User = get_user_model()


class CreateStaffMember(CreateAPIView):
    """ Create a new staff member """

    permission_classes = [IsAdminPermission]
    serializer_class = StaffMemberSerializer
    queryset = User.objects.all()
