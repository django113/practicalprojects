from django.contrib.auth import get_user_model
from django.db import models

from ORDER.models import Order

User = get_user_model()


class AssignedOrder(models.Model):
    delivery_executive = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_executive')
    orders = models.ManyToManyField(Order)
    delivery_datetime = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.delivery_executive)

    class Meta:
        db_table = 'tbl_assigned_order'
