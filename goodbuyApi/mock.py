from django.http import HttpResponse, JsonResponse
import json

def feedback(self, code):
    response = {}
    if code == 11111111:
        return HttpResponse(status=209)
    elif code == 22222222:
        return HttpResponse(status=209)
    elif code == 33333333:
        response = {
            'is_big_ten': True,
            'fields': {
                'name': 'Mock Product',
                'brand': 'Mock Brand',
                'corporation': 'Mock Corporation'
            },
        }
    elif code == 44444444:
        response = {
            'is_big_ten': False,
            'fields': {
                'name': 'Mock Product',
                'brand': 'Mock Brand',
                'corporation': 'Mock Corporation'
            },
        }
    elif code == 55555555:
        response = {
            'is_big_ten': None,
            'fields': {
                'name': 'Mock Product',
                'brand': None,
                'corporation': 'Mock Corporation'
            },
        }
        return JsonResponse(response, status=210)
    elif code == 66666666:
        return HttpResponse(status=211)
    return JsonResponse(response)

def result(self, code):
    if code == 11111111:
        response = {
            'is_big_ten': True,
            'fields': {
                'name': 'Mock Product',
                'brand': 'Mock Brand',
                'corporation': 'Mock Corporation'
            },
        }
    if code == 22222222:
        response = {
            'is_big_ten': False,
            'fields': {
                'name': 'Mock Product',
                'brand': 'Mock Brand',
                'corporation': 'Mock Corporation'
            },
        }
    return JsonResponse(response)

def current_categories(self):
    response = [{'name': 'Fish'}, {'name': 'Drinks'}, {'name': 'Meat'}]
    return JsonResponse(response, safe=False)

def product_validation(self, params):
    return JsonResponse(params, status=200)
