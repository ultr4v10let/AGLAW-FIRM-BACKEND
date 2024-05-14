from rest_framework import generics
from legalservices.models import LegalServices
from legalservices.serializer import LegalServicesSerializer

class LegalServicesList(generics.ListAPIView):
    serializer_class = LegalServicesSerializer
    queryset = LegalServices.objects.get_queryset()