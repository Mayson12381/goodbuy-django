from django.shortcuts import get_object_or_404, render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


@permission_classes([AllowAny])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer


@permission_classes([AllowAny])
class product_by_code(generics.ListCreateAPIView):
    def get_queryset(self):
        return Product.objects.filter(barcode=self.kwargs["pk"])
    serializer_class = ProductSerializer


@permission_classes([AllowAny])
class product_by_id(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
