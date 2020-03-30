from django.forms.models import model_to_dict

def getFeedbackProduct(product, isBlacklisted):
  product_as_dict = model_to_dict(product)
  if isBlacklisted != '':
    product_as_dict['is_blacklist'] = isBlacklisted
  return product_as_dict

from .models import Product, Corporation

def isBigTen(brand):
  print(brand)
  if brand is None:
    return
  brandObjectExists = Brand.objects.filter(name=brand).exists()
  if brandObjectExists:
    brandObject = Brand.objects.get(name=brand)
    if brandObject.corporation:
      return Corporation.objects.filter(name=brandObject.corporation, is_big_ten=True).exists()
  return False


def getCorporation(brand):
  if brand is None:
    return ''
  brandObjectExists = Brand.objects.filter(name=brand).exists()
  if brandObjectExists:
    brandObject = Brand.objects.get(name=brand)
    if brandObject.corporation:
      return brandObject.corporation
  return ''


def isBlacklisted(brand, blacklist):
  if brand is None:
    return
  brandObjectExists = Brand.objects.filter(name=brand).exists()
  if brandObjectExists:
    brandObject = Brand.objects.get(name=brand)
    if brandObject.corporation:
      return brandObject.corporation in blacklist
  return ''

import json
from .models import Brand
from django.http import HttpResponse

def migrateBrands(self):
  with open('goodbuyApi/big_ten_brands.json') as json_file:
    data = json.load(json_file)
    for brand in data:
      isBrandAccessable = Brand.objects.filter(name=brand['name']).exists()

      if isBrandAccessable and Brand.objects.get(name=brand['name']).corporation == "":
        brandObject = Brand.objects.get(name=brand['name'])
        brandObject.corporation = brand['corporation_id']
        brandObject.save()
      elif not isBrandAccessable and brand['name'] and brand['corporation_id']:
        Brand.objects.create(name=brand['name'], corporation=brand['corporation_id'])

  return HttpResponse(status=200)
  

