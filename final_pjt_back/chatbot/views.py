from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import *
from .serializers import SavingProductSerializer, DepositProductSerializer, PortfolioSerializer
import pandas as pd
import re

def extract_keywords(message):
    keywords = re.findall(r'\b\w+\b', message.lower())
    return keywords

@api_view(['POST'])
def chatbot(request):
    user_message = request.data.get('message')
    user_info = request.data.get('user')

    age = user_info.get('age')
    current_balance = user_info.get('current_balance')
    annual_salary = user_info.get('annual_salary')
    saving_preference = user_info.get('saving_preference')
    favorite_bank = user_info.get('favorite_bank')

    keywords = extract_keywords(user_message)

    saving_products = SavingProducts.objects.all()
    deposit_products = DepositProducts.objects.all()
    if age is not None:
        if 'saving' in keywords or '적금' in keywords:
            saving_products = saving_products.filter(age_min__lte=age, age_max__gte=age)
        if 'deposit' in keywords or '예금' in keywords:
            deposit_products = deposit_products.filter(age_min__lte=age, age_max__gte=age)

    if favorite_bank:
        saving_products = saving_products.filter(bank__icontains=favorite_bank)
        deposit_products = deposit_products.filter(bank__icontains=favorite_bank)

    # Convert queryset to dataframe
    saving_df = pd.DataFrame(list(saving_products.values()))
    deposit_df = pd.DataFrame(list(deposit_products.values()))

    # Recommendations based on user profile
    saving_recommendations = saving_df.head(10).to_dict('records') if not saving_df.empty else []
    deposit_recommendations = deposit_df.head(10).to_dict('records') if not deposit_df.empty else []

    # Prepare response message
    response_message = "Recommended products based on your profile:\n\nSaving Products:\n"
    if saving_recommendations:

        for product in saving_recommendations:
            response_message += f"- {product['fin_prdt_nm']} \n"
    else:
        response_message += "No saving products found.\n"

    response_message += "\nDeposit Products:\n"
    if deposit_recommendations:
        for product in deposit_recommendations:
            response_message += f"- {product['fin_prdt_nm']} \n"
    else:
        response_message += "No deposit products found.\n"

    return Response({"reply": response_message})
