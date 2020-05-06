import json

import requests
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from . import utils
from .models import Blacklist, Brand, Product


def getUserBlacklist(user_id):
    if user_id != '':
        isBlacklistExisting = Blacklist.objects.filter(
            user_id=user_id).exists()
        if isBlacklistExisting:
            return Blacklist.objects.get(user_id=user_id).blacklist.split(',')
    return []


def getExistingProduct(user_id, blacklist, barcode, scanned=False):
    product = Product.objects.get(barcode=barcode)
    if scanned:
        product.scanned_counter += 1
    product.save()
    if product.state == 209:
        return JsonResponse(utils.getFeedbackProduct(product, ''), status=209)
    if user_id != '':
        isBlacklist = utils.isBlacklisted(product.brand, blacklist)
    else:
        isBlacklist = ''
    return utils.getFeedbackProduct(product, isBlacklist)


def getOFFProduct(OFFResponse_json, barcode, blacklist, user_id):
    try:
        brand, _ = Brand.objects.get_or_create(
            name=OFFResponse_json["product"]["brands"]
        )
        state = 200
    except Exception as e:
        print(str(e))
        brand = None
        state = 306
    try:
        Product.objects.create(
            name=OFFResponse_json["product"]["product_name"],
            brand=brand,
            corporation=utils.getCorporation(brand),
            barcode=barcode,
            is_big_ten=utils.isBigTen(brand),
            state=state,
        )

        product = Product.objects.get(barcode=barcode)
        if user_id != '':
            isBlacklist = utils.isBlacklisted(product.brand, blacklist)
        else:
            isBlacklist = ''
        return utils.getFeedbackProduct(product, isBlacklist)
    except Exception as e:
        print(str(e))


@api_view(['GET'])
@permission_classes([AllowAny])
def instant_feedback(request, barcode):
    user_id = request.query_params['user_id']
    blacklist = getUserBlacklist(user_id)

    # ! get existing Product
    isProductAccessable = Product.objects.filter(barcode=barcode).exists()
    if isProductAccessable:
        return JsonResponse(
            getExistingProduct(
                user_id,
                blacklist,
                barcode,
                scanned=True))

    # ! OFF Request
    OFFResponse = requests.get(
        f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    )
    OFFResponse_json = json.loads(OFFResponse.text)
    if OFFResponse_json["status_verbose"] == "product found":
        return JsonResponse(getOFFProduct(OFFResponse_json, barcode, blacklist, user_id))

    # ! CC Crawler via AWS
    else:
        Product.objects.create(barcode=barcode, state="209")
        params = {"barcode": barcode}
        try:
            requests.post(
                "https://jr08d16pid.execute-api.eu-central-1.amazonaws.com/prod/",
                params=params,
                timeout=1,
            )
        except Exception as e:
            print(str(e))
            pass
        return HttpResponse(status=209)
    return HttpResponse(status=500)


@api_view(['GET'])
@permission_classes([AllowAny])
def instant_feedback_result(request, barcode):
    user_id = request.query_params['user_id']
    blacklist = getUserBlacklist(user_id)

    isProductAccessable = Product.objects.filter(barcode=barcode).exists()
    if isProductAccessable:
        return getExistingProduct(user_id, blacklist, barcode, scanned=False)


@api_view(['GET'])
@permission_classes([AllowAny])
def feedback_fridge_karma(request):
    user_id = request.query_params['user_id']
    barcodes = request.query_params['barcodes'].split(',')
    blacklist = getUserBlacklist(user_id)
    responseList = []

    print(barcodes)

    for barcode in barcodes:
        isProductAccessable = Product.objects.filter(barcode=barcode).exists()
        if isProductAccessable:
            responseList.append(getExistingProduct(user_id, blacklist, barcode, scanned=True))
            continue

        OFFResponse = requests.get(
            f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
        )
        OFFResponse_json = json.loads(OFFResponse.text)
        if OFFResponse_json["status_verbose"] == "product found":
            responseList.append(
                getOFFProduct(
                    OFFResponse_json,
                    barcode,
                    blacklist,
                    user_id))
            continue

        else:
            Product.objects.create(barcode=barcode, state="209")
            params = {"barcode": barcode}
            try:
                requests.post(
                    "https://jr08d16pid.execute-api.eu-central-1.amazonaws.com/prod/",
                    params=params,
                    timeout=1,
                )
            except Exception as e:
                print(str(e))
                pass
            responseList.append({'barcode': barcode})
            continue
        responseList.append({'barcode': barcode})
    print(responseList)
    return JsonResponse(responseList, safe=False)


@api_view(['GET'])
@permission_classes([AllowAny])
def voteProduct(request, barcode):
    vote = request.query_params['vote']
    product = Product.objects.get(barcode=barcode)
    if vote == 'upvote':
        product.upvote_counter += 1
    elif vote == 'downvote':
        product.downvote_counter += 1
    product.save()
    return HttpResponse(200)
