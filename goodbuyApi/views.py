from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.views import APIView

from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

class product_by_code(generics.ListAPIView):
    def get_queryset(self):
        code = self.kwargs['code']
        return Product.objects.filter(barcode=code)
    serializer_class = ProductSerializer

class product_by_id(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
