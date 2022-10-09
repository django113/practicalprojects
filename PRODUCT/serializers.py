from rest_framework import serializers
from .models import Category, Product, ProductImage
from ORDER.models import OrderDetails


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'image', 'name', 'MRP', 'price', 'category', 'quantity', 'description']

    def create(self, validated_data):
        images = self.context["request"].FILES
        product = Product.objects.create(**validated_data)

        for image in images.getlist("image"):
            ProductImage.objects.create(image=image, product=product)

        return product

    def update(self, instance, validated_data):
        images = self.context["request"].FILES
        product = super(ProductDetailSerializer, self).update(instance, validated_data)
        ProductImage.objects.filter(product=product).delete()

        for image in images.getlist("image"):
            ProductImage.objects.create(image=image, product=product)

        return product

    def get_image(self, obj):
        return ProductImage.objects.filter(product=obj).values_list('image', flat=True)


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'image', 'name', 'MRP', 'price', 'category', 'quantity', 'description']

    def get_image(self, obj):
        return ProductImage.objects.filter(product=obj).values_list('image', flat=True)


class OrderProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'image', 'name', 'MRP', 'price']

    def get_image(self, obj):
        return ProductImage.objects.filter(product=obj).values_list('image', flat=True)[0]
