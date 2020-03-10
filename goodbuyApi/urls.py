from django.urls import include, path
from rest_framework import routers
from . import views, mock

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product/barcode/<int:pk>/', views.product_by_code.as_view(), name='product_by_code'),
    path('product/id/<int:pk>/', views.product_by_id.as_view(), name='product_by_id'),

    # mock endpoints
    path('feedback/<int:code>', mock.feedback),
    path('feedback/result/<int:code>', mock.result),
    path('goodbuyDatabase/current_categories/', mock.current_categories),
    path('goodbuyDatabase/product_validation/', mock.product_validation),
    path('goodbuyDatabase/update_product/', mock.update_product),
    path('goodbuyDatabase/fridge_karma_feedback/', mock.feedback_fridge_karma),
]
