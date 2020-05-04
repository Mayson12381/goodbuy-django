from django.urls import include, path
from rest_framework import routers
from . import views, endpoint_functions, utils

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('corporations', views.CorporationViewSet)
router.register('brands', views.BrandViewSet)
router.register('categories', views.CategoryViewSet)
router.register('blacklists', views.BlacklistViewSet)
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),

    path('migrate', utils.migrateBrands),

    path(
        'instant_feedback/<int:barcode>',
        endpoint_functions.instant_feedback
    ),
    path(
        'instant_feedback/result/<int:barcode>',
        endpoint_functions.instant_feedback_result
    ),

    path('fridge_karma/', endpoint_functions.feedback_fridge_karma),

    path('products/<int:barcode>/vote/', endpoint_functions.voteProduct),
]
