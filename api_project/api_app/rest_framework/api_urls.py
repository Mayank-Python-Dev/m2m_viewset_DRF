from django.conf.urls import url, include
from .api_views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("product_api", ProductViewSet, basename="product")


urlpatterns = [
    url("", include(router.urls))
]
