from django.contrib import admin
from django.utils.html import format_html
from .models import Product, ProductImage, Category


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['category', 'id']


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['name', 'category', 'MRP', 'price', 'quantity', 'datetimestamp']


@admin.register(ProductImage)
class ProductImage(admin.ModelAdmin):
    list_display = ['product', 'image_link']

    def image_link(self, obj):
        return format_html("<a href='{url}' target='_blank'>{url}</a>", url=obj.image.url)
