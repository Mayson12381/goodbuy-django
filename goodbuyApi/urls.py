from django.urls import include, path
from rest_framework import routers
from . import views, mock, feedback, utils

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

    path('instant_feedback/<int:barcode>', feedback.instant_feedback),
    path('instant_feedback/result/<int:barcode>', feedback.instant_feedback_result),

    path('fridge_karma/', feedback.feedback_fridge_karma),

    path('products/<int:barcode>/vote/', feedback.voteProduct),
    
    # mock endpoints
    # path('mock/feedback/<int:barcode>', mock.feedback),
    # path('mock/feedback/result/<int:code>', mock.result),
    # path('mock/goodbuyDatabase/current_categories/', mock.current_categories),
    # path('mock/goodbuyDatabase/product_validation/', mock.product_validation),
    # path('mock/goodbuyDatabase/update_product/', mock.update_product),
    # path('mock/goodbuyDatabase/fridge_karma_feedback/',
    #      mock.feedback_fridge_karma),
]
