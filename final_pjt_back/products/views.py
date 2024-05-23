from rest_framework.response import Response
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import DepositProductsSerializer, SavingProductsSerializer
from .models import *

@api_view(['GET', 'POST'])
def depositproducts_list(request):
    if request.method == 'GET':
        depositproducts = DepositProducts.objects.all()
        serializers = DepositProductsSerializer(depositproducts, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def savingproducts_list(request):
    if request.method == 'GET':
        savingproducts = SavingProducts.objects.all()
        serializers = SavingProductsSerializer(savingproducts, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = SavingProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def depositproduct_detail(request, pk):
    depositproduct = get_object_or_404(DepositProducts, pk=pk)
    if request.method == 'GET':
        serializer = DepositProductsSerializer(depositproduct)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DepositProductsSerializer(depositproduct, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        depositproduct.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def savingproduct_detail(request, pk):
    savingproduct = get_object_or_404(SavingProducts, pk=pk)
    if request.method == 'GET':
        serializer = SavingProductsSerializer(savingproduct)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SavingProductsSerializer(savingproduct, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        savingproduct.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PopularOptionsView(APIView): # 필요한 경우 인증 설정

    def get(self, request, *args, **kwargs):
        most_popular_deposit_option = DepositOptions.objects.annotate(num_users=Count('users')).order_by('-num_users').first()
        most_popular_saving_option = SavingOptions.objects.annotate(num_users=Count('users')).order_by('-num_users').first()

        data = {
            'most_popular_deposit_option': {
                'bank': most_popular_deposit_option.product.kor_co_nm,
                'name': most_popular_deposit_option.product.fin_prdt_nm,
                'num_users': most_popular_deposit_option.num_users,
            } if most_popular_deposit_option else None,
            'most_popular_saving_option': {
                'bank': most_popular_saving_option.product.kor_co_nm,
                'name': most_popular_saving_option.product.fin_prdt_nm,
                'num_users': most_popular_saving_option.num_users,
            } if most_popular_saving_option else None,
        }

        return Response(data)