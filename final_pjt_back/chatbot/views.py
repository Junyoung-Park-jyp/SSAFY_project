import openai
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
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
    saving_options = SavingOptions.objects.all()
    deposit_options = DepositOptions.objects.all()
    # Recommendations based on user profile
    
    if 'saving' in keywords or '예금' in keywords or 'deposit' in keywords or '적금' in keywords or '상품' in keywords:
        # Prepare response message with recommendations
        top_deposit = deposit_options.order_by('-intr_rate').first()
        top_saving = saving_options.order_by('-intr_rate').first()
        popular_deposit = deposit_options.annotate(num_users=Count('users')).order_by('-num_users').first()
        popular_saving = saving_options.annotate(num_users=Count('users')).order_by('-num_users').first()
        response_message = ''
        if '최고' in keywords or '금리' in keywords:
            response_message += "최고 금리 상품입니다."
            response_message += "\n적금 상품:\n"
            response_message += f"{top_saving.product.kor_co_nm} - {top_saving.product}{top_saving.intr_rate}% \n"
            response_message += "\n예금 상품:\n"
            response_message += f"{top_deposit.product.kor_co_nm} - {top_deposit.product}{top_deposit.intr_rate}% \n"
        if '사람들' in keywords or '가입자' in keywords or '가입수' in keywords:
            response_message = "최다 가입자 상품입니다."
            response_message += "\n적금 상품:\n"
            response_message += f"{popular_saving.product.kor_co_nm} - {popular_saving.product} \n"
            response_message += "\n예금 상품:\n"
        response_message += f"{popular_deposit.product.kor_co_nm} - {popular_deposit.product}% \n\n\n"        
        response_message += "회원정보를 바탕으로 추천해드리는 상품입니다."
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
        saving_recommendations = saving_df.head(10).to_dict('records') if not saving_df.empty else []
        deposit_recommendations = deposit_df.head(10).to_dict('records') if not deposit_df.empty else []
        
        if saving_recommendations:
            response_message += "\n\n적금 상품:\n"
            for product in saving_recommendations:
                response_message += f"{bank} - {product['fin_prdt_nm']} \n"


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