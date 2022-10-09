from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class DeliveryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='delivery_user')
    city = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    vehicle_number = models.CharField(max_length=15)

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'tbl_delivery_user'
