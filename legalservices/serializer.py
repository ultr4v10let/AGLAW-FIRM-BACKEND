
from rest_framework import serializers
from legalservices.models import LegalServices

class LegalServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalServices
        fields = '__all__'