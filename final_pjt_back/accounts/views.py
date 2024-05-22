from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
def user_info(request):
    if request.method == 'POST':
        user = request.user  # 요청을 보낸 사용자의 정보를 가져옴
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)  # 요청을 보낸 사용자 정보를 저장
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_info(request):
    user = request.user
    user_info, created = UserInfo.objects.get_or_create(user=user)
    serializer = UserInfoSerializer(user_info, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def add_deposit(request):
    user = request.user
    user_info, created = UserInfo.objects.get_or_create(user=user)
    deposit_option_id = request.data.get('pk')
    if deposit_option_id:
        try:
            deposit_option = DepositOptions.objects.get(id=deposit_option_id)
            user_info.deposit_options.add(deposit_option)
            user_info.save()
            return Response({'status': 'Deposit product added'}, status=status.HTTP_200_OK)
        except DepositOptions.DoesNotExist:
            return Response({'error': 'Deposit product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    return Response({'error': 'No deposit product ID provided'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def add_saving(request):
    user = request.user
    user_info, created = UserInfo.objects.get_or_create(user=user)
    saving_option_id = request.data.get('pk')
    if saving_option_id:
        try:
            saving_option = SavingOptions.objects.get(id=saving_option_id)
            user_info.saving_options.add(saving_option)
            user_info.save()
            return Response({'status': 'Saving product added'}, status=status.HTTP_200_OK)
        except SavingOptions.DoesNotExist:
            return Response({'error': 'Saving product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    return Response({'error': 'No saving product ID provided'}, status=status.HTTP_400_BAD_REQUEST)
