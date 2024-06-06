from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdLocationViewSet, AdSpendViewSet, BusinessCryptoViewSet

router = DefaultRouter()
router.register(r'locations', AdLocationViewSet)
router.register(r'adSpends', AdSpendViewSet)
router.register(r'businessCryptos', BusinessCryptoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
