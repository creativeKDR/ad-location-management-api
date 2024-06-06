from rest_framework import viewsets
from .models import AdLocation, AdSpend, BusinessCrypto
from .serializers import AdLocationSerializer, AdSpendSerializer, BusinessCryptoSerializer


class AdLocationViewSet(viewsets.ModelViewSet):
    queryset = AdLocation.objects.all()
    serializer_class = AdLocationSerializer


class AdSpendViewSet(viewsets.ModelViewSet):
    queryset = AdSpend.objects.all()
    serializer_class = AdSpendSerializer


class BusinessCryptoViewSet(viewsets.ModelViewSet):
    queryset = BusinessCrypto.objects.all()
    serializer_class = BusinessCryptoSerializer
