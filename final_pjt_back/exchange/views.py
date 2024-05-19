import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ExchangeRateSerializer

@api_view(['GET'])
def get_exchange_rate(request):
    try:
        response = requests.get('https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=rhw2ldfOz9zngLX1vFIFFjwEUWwHBBWi&searchdate=20240516&data=AP01')
        data = response.json()
        
        exchange_rates = []
        for item in data:
            exchange_rates.append({
                'currency': item['cur_unit'],
                'rate': float(item['deal_bas_r'].replace(',', ''))
            })
        
        serializer = ExchangeRateSerializer(exchange_rates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
