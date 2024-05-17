from rest_framework import serializers

class ExchangeRateSerializer(serializers.Serializer):
    currency = serializers.CharField()
    rate = serializers.FloatField()
