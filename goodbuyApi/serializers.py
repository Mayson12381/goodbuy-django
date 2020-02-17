from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'brand', 'cooperation', 'barcode', 'name', 'is_big_ten')
