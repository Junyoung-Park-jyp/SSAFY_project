from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import SavingProducts, DepositProducts
from products.serializers import SavingProductsSerializer, DepositProductsSerializer

@api_view(['POST'])
def chatbot(request):
    user_message = request.data.get('message')
    user_info = request.data.get('user')

    age = user_info.get('age')
    bank = user_info.get('bank')

    # 나이와 은행을 기준으로 상품 추천
    savings = SavingProducts.objects.filter(age_min__lte=age, age_max__gte=age, bank=bank)
    deposits = DepositProducts.objects.filter(age_min__lte=age, age_max__gte=age, bank=bank)

    saving_serializer = SavingProductsSerializer(savings, many=True)
    deposit_serializer = DepositProductsSerializer(deposits, many=True)

    response_message = f"나이 {age}세이고 {bank} 은행을 이용하시는 고객님께 추천드리는 상품은 다음과 같습니다:\n"
    response_message += "적금 상품:\n"
    for product in saving_serializer.data:
        response_message += f"- {product['name']} ({product['interest_rate']}%)\n"

    response_message += "예금 상품:\n"
    for product in deposit_serializer.data:
        response_message += f"- {product['name']} ({product['interest_rate']}%)\n"

    return Response({"reply": response_message})
