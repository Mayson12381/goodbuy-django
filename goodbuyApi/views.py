import json

import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Blacklist, Brand, Category, Corporation, Product
from .serializers import (BlacklistSerializer, BrandSerializer,
                          CategorySerializer, CorporationSerializer,
                          ProductSerializer)


@permission_classes([AllowAny])
class BlacklistViewSet(viewsets.ModelViewSet):
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer
    lookup_field = 'user_id'

    def get_permissions(self):
        return [permission() for permission in [IsAuthenticated]]

@permission_classes([AllowAny])
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('name')
    serializer_class = BrandSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

@permission_classes([AllowAny])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

@permission_classes([AllowAny])
class CorporationViewSet(viewsets.ModelViewSet):
    queryset = Corporation.objects.all().order_by('name')
    serializer_class = CorporationSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

@permission_classes([AllowAny])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    lookup_field = 'barcode'

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
