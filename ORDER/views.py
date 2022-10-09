from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError, NotFound
from ACCOUNT.models import DeliveryAddress
from ACCOUNT.serializers import DeliveryAddressSerializer
from PRODUCT.models import Product
from PRODUCT.serializers import ProductSerializer
from .serializers import OrderDetailSerializer
from .models import Order, OrderDetails


class CreateOrderView(APIView):
    """ Generating Order for product by user """

    permission_classes = [IsAuthenticated]

    def __init__(self):
        self.items = {}
        super(CreateOrderView, self).__init__()

    def get_amount(self):
        return sum([product.price * quantity for product, quantity in self.items.items()])

    def check_quantity(self, products):
        for product in products:
            if product.quantity <= 0:
                return False
        return True

    def update_stock(self):
        for product, count in self.items.items():
            product.quantity -= count
            product.save()

    def create_order(self, address, products):

        order = Order.objects.create(
            user=self.request.user,
            address=address,
            amount=self.get_amount(),
            status='success',
            delivery_status='ordered'
        )
        self.update_stock()

        for product, quantity in self.items.items():
            OrderDetails.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )

        for product in products:
            order.product.add(product)

        order.save()
        return order

    def post(self, request, *args, **kwargs):
        product_list = []
        items = request.data.get('product', {})

        try:
            address = DeliveryAddress.objects.get(id=request.data.get('address'))
            for product, quantity in items.items():
                self.items.update({Product.objects.get(id=product): quantity})
                product_list.append(Product.objects.get(id=product))

        except (DeliveryAddress.DoesNotExist, Product.DoesNotExist) as error:
            raise ValidationError({"details": error})

        if self.check_quantity(product_list):
            order = self.create_order(address, product_list)
            res = {
                'id': order.id,
                'amount': order.amount,
                'status': order.status,
                'delivery_status': order.delivery_status,
                'datetimestamp': order.datetimestamp,
                'address': DeliveryAddressSerializer(order.address).data,
                'products': [ProductSerializer(item).data for item in order.product.all()]
            }
            return Response(data=res)

        else:
            raise ValidationError({'details': 'item is out of stock'})


class UserOrderListView(ListAPIView):
    """ Display the order history of an individual user """

    permission_classes = [IsAuthenticated]
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class UserOrderDetailView(RetrieveAPIView):
    """ Return the info of particular order """

    permission_classes = [IsAuthenticated]
    serializer_class = OrderDetailSerializer

    def get_object(self):
        try:
            return Order.objects.get(id=self.kwargs.get('id'))
        except Order.DoesNotExist as error:
            raise NotFound
