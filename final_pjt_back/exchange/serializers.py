from rest_framework import serializers
from .models import *
class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ['currency', 'rate', 'country_name_ko', 'country_name_en']
