from django.urls import include, path
from rest_framework import routers
from . import views, scripts

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("product/barcode/<int:pk>/", views.product_by_code.as_view(), name="product_by_code"),
    path("product/id/<int:pk>/", views.product_by_id.as_view(), name="product_by_id"),

    # mock endpoints
    path('feedback/<int:code>', scripts.feedback)
    # /feedback/result/
]
