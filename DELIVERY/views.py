from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import exceptions as permission
from rest_framework.response import Response
from LOGISTIC.models import AssignedOrder
from LOGISTIC.serializers import OrderLogisticSerializer
from ORDER.models import Order
from .serializers import AttendanceSerializer
from .models import Attendance


class MarkAttendanceView(CreateAPIView):
    """ Mark attendance API for delivery user """

    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()

    def get_serializer_context(self):
        self.check_permissions(self.request)
        context = super(MarkAttendanceView, self).get_serializer_context()
        context['user'] = self.request.user
        return context

    def check_permissions(self, request):
        if self.request.user.is_authenticated and self.request.user.is_staff and self.request.user.type == 'delivery':
            pass
        else:
            raise permission.PermissionDenied


class DeliveryOrderView(ListAPIView):
    """ Display the assigned order to delivery executive """

    def __init__(self):
        super(DeliveryOrderView, self).__init__()
        self.res = {"message": "in development"}

    def get(self, request, *args, **kwargs):
        self.check_permissions(request)
        queryset = AssignedOrder.objects.filter(delivery_executive=self.request.user)

        for order in queryset:
            print(order.orders.all().values_list('product__orderdetails'))

        return Response(self.res)

    def check_permissions(self, request):
        if self.request.user.is_authenticated and self.request.user.is_staff and self.request.user.type == 'delivery':
            pass
        else:
            raise permission.PermissionDenied
