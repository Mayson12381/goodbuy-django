from django.http import HttpResponse, JsonResponse
import json

def feedback(self, code):
    response = {
        'is_big_ten': False,
        'code': code,
    }
    return JsonResponse(response)
