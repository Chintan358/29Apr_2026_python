from django.urls import *
from eshop.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register("categories",CategoryViewSet,basename="categories")
router.register("products",ProductViewSet,basename="products")
urlpatterns = [
    path('', include(router.urls)),
]