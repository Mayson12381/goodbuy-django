from django.contrib import admin
from .models import Product, Corporation, Brand, Category

admin.site.register(Product)
admin.site.register(Corporation)
admin.site.register(Brand)
admin.site.register(Category)
