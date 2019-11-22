from django.db import models

class Product(models.Model):
    brand = models.CharField(max_length=100)
    cooperation = models.CharField(max_length=100)
    barcode = models.CharField(max_length=13)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
