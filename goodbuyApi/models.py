from django.db import models


class Blacklist(models.Model):
    # owner = models.ForeignKey(
    #     'auth.User', related_name='blacklists', on_delete=models.CASCADE)
    user_id = models.CharField(unique=True, max_length=100)
    blacklist = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.user_id


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    corporation = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return self.name


class Corporation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500, blank=True, default='')
    is_big_ten = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.CharField(max_length=100)
    corporation = models.CharField(max_length=100, default='')
    barcode = models.CharField(max_length=13, unique=True)
    name = models.CharField(max_length=100)
    is_big_ten = models.BooleanField(default=False, null=True)
    scanned_counter = models.IntegerField(default=0)
    state = models.IntegerField(default=200)
    upvote_counter = models.IntegerField(default=0)
    downvote_counter = models.IntegerField(default=0)
    # category = models.ForeignKey(
    #     Category,
    #     models.SET_NULL,
    #     verbose_name="Main Product Category",
    #     null=True,
    #     blank=True,
    # )

    def __str__(self):
        return self.name
