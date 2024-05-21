import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ExchangeRateSerializer
from .models import ExchangeRate

@api_view(['GET'])
def get_exchange_rate(request):
    try:
        response = requests.get('https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=rhw2ldfOz9zngLX1vFIFFjwEUWwHBBWi&searchdate=20240516&data=AP01')
        data = response.json()
        
        exchange_rates = []
        for item in data:
            exchange_rate, created = ExchangeRate.objects.update_or_create(
                currency=item['cur_unit'],
                defaults={
                    'rate': float(item['deal_bas_r'].replace(',', '')),
                    'country_name_ko': item['cur_nm'].split(' ')[0],  # 한국어 이름만 분리
                    'country_name_en': item['cur_nm'].split(' ')[-1]  # 영어 이름만 분리
                }
            )
            exchange_rates.append(exchange_rate)
        
        serializer = ExchangeRateSerializer(exchange_rates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
