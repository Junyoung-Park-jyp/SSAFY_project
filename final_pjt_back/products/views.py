from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import DepositProductsSerializer, SavingProductsSerializer
from .models import DepositProducts, SavingProducts

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
