import pyotp
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """ custom user model """

    USER = [
        ('admin', _('ADMIN USER')),
        ('manager', _('WAREHOUSE MANAGER')),
        ('delivery', _('DELIVERY USER')),
        ('user', _('USER'))
    ]

    username = None
    first_name = None
    last_name = None
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=10, unique=True, null=False, blank=False)
    type = models.CharField(max_length=50, choices=USER, default='user')
    key = models.CharField(max_length=128, default=pyotp.random_base32)
    last_otp = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    def create_user(self):
        pass

    class Meta:
        db_table = 'tbl_user'
        verbose_name = 'User'
        ordering = ['-date_joined']


class DeliveryAddress(models.Model):
    """ store the delivery address information """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_delivery_address')
    area = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return " ".join([self.area, self.city, self.state, self.pincode])

    class Meta:
        db_table = 'tbl_address'
        verbose_name = 'Address'
        ordering = ['-area']
