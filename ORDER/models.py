import uuid
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from ACCOUNT.models import DeliveryAddress
from PRODUCT.models import Product

User = get_user_model()


def generate_order_id():
    return uuid.uuid4().hex


class Order(models.Model):
    STATUS = [
        ('success', _('SUCCESS')),
        ('pending', _('PENDING')),
        ('failed', _('FAILED')),
    ]

    DELIVERY_STATUS = [
        ('ordered', _('ORDERED')),
        ('pick_up', _('PICKED UP')),
        ('in_transit', _('IN TRANSIT')),
        ('out_for_delivery', _('OUT FOR DELIVERY')),
        ('delivered', _('DELIVERED')),
        ('returned', 'RETURNED')
    ]

    id = models.CharField(verbose_name='ORDER ID', max_length=64, default=generate_order_id, editable=False, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user', editable=False)
    product = models.ManyToManyField(Product, related_name='order_product')
    address = models.ForeignKey(DeliveryAddress, on_delete=models.CASCADE, related_name='order_address')
    amount = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    datetimestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS)
    delivery_status = models.CharField(max_length=10)

    class Meta:
        db_table = 'tbl_order'
        ordering = ['-datetimestamp']

    def __str__(self):
        return self.id


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'tbl_order_detail'

    def __str__(self):
        return self.product.name
