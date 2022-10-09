from rest_framework.generics import ListAPIView, CreateAPIView
from STAFF.permissions import StaffPermission
from LOGISTIC.serializers import OrderLogisticSerializer, AssignOrderSerializer
from ORDER.models import Order


class AllOrderListView(ListAPIView):
    """ Display the list of most generated order """

    permission_classes = [StaffPermission]
    serializer_class = OrderLogisticSerializer
    queryset = Order.objects.all().exclude(product__order_product__delivery_status='delivered').order_by('-datetimestamp')


class AssignOrderView(CreateAPIView):
    """ A staff member can assign the order to delivery executive """

    permission_classes = [StaffPermission]
    serializer_class = AssignOrderSerializer
