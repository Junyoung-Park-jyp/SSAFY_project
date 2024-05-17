import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def search_banks(request):
    try:
        location = request.query_params.get('location', '37.5665,126.9780')
        bank_name = request.query_params.get('bank_name', '우리은행')
        if not location or not bank_name:
            return Response({'error': 'Location and bank_name parameters are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        kakao_api_key = 'e4396d82b327c4c6338c9b6f486f29ee'
        url = f'https://dapi.kakao.com/v2/local/search/keyword.json?query={bank_name}&x={location.split(",")[1]}&y={location.split(",")[0]}&radius=20000'
        headers = {
            'Authorization': f'KakaoAK {kakao_api_key}'
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
