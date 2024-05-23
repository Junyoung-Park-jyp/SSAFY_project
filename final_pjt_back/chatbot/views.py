import openai
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import *
import pandas as pd
import re
import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI API 키 설정
openai.api_key = os.getenv('OPENAI_API_KEY')

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
    bank = user_info.get('bank')
    keywords = extract_keywords(user_message)

    saving_products = SavingProducts.objects.all()
    deposit_products = DepositProducts.objects.all()
    if age is not None:
        if 'saving' in keywords or '예금' in keywords:
            saving_products = saving_products.filter(age_min__lte=age, age_max__gte=age)
        if 'deposit' in keywords or '적금' in keywords:
            deposit_products = deposit_products.filter(age_min__lte=age, age_max__gte=age)

    if bank:
        saving_products = saving_products.filter(kor_co_nm=bank)
        deposit_products = deposit_products.filter(kor_co_nm=bank)

    # Convert queryset to dataframe
    saving_df = pd.DataFrame(list(saving_products.values()))
    deposit_df = pd.DataFrame(list(deposit_products.values()))
    print(deposit_df)
    # Recommendations based on user profile
    saving_recommendations = saving_df.head(10).to_dict('records') if not saving_df.empty else []
    deposit_recommendations = deposit_df.head(10).to_dict('records') if not deposit_df.empty else []
    print(deposit_recommendations)
    if 'saving' in keywords or '예금' in keywords or 'deposit' in keywords or '적금' in keywords:
        # Prepare response message with recommendations
        response_message = "회원정보를 바탕으로 추천해드리는 상품입니다."
        if saving_recommendations:
            response_message += "\n\n적금 상품:\n"
            for product in saving_recommendations:
                response_message += f"- {product['fin_prdt_nm']} \n"


        elif deposit_recommendations:
            response_message += "\n예금상품:\n"
            for product in deposit_recommendations:
                response_message += f"- {product['fin_prdt_nm']} \n"
        else:
            response_message += "상품이 없다.\n"
    else:
        # Call OpenAI API for general responses using the new interface
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message},
                ],
                max_tokens=150,
                temperature=0.7,
            )
            response_message = response.choices[0].message['content'].strip()
        except openai.error.OpenAIError as e:
            response_message = f"An OpenAI error occurred: {str(e)}"
        except Exception as e:
            response_message = f"An unexpected error occurred: {str(e)}"

    return Response({"reply": response_message})