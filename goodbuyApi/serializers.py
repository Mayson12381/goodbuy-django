from rest_framework import serializers

from .models import Product, Corporation, Brand, Category, Blacklist

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')


class CorporationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporation
        fields = ('__all__')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blacklist
        fields = ('__all__')
