from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.views import APIView

from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

class product_by_code(generics.ListCreateAPIView):
    def get_queryset(self):
        return Product.objects.filter(barcode=self.kwargs["pk"])
    serializer_class = ProductSerializer

class product_by_id(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
