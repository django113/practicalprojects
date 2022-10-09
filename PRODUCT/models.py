from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


def get_image_path(instance, filename):
    return "product/%s/%s" % (instance.product.category, filename)


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category

    class Meta:
        db_table = 'tbl_category'
        verbose_name_plural = 'Categories'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    MRP = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100000)])
    price = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100000)])
    quantity = models.IntegerField()
    description = models.TextField()
    datetimestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_product'
        ordering = ['-datetimestamp']


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_path)

    def __str__(self):
        return str(self.product.name)

    class Meta:
        db_table = 'tbl_product_image'
