from rest_framework import serializers
from .models import *
from products.serializers import *

class UserInfoSerializer(serializers.ModelSerializer):
    deposit_options = DepositOptionsSerializer(many=True, read_only=True)
    saving_options = SavingOptionsSerializer(many=True, read_only=True)
    class Meta:
        model = UserInfo
        fields = '__all__'
        read_only_fields = ['user']

class UserSerializer(serializers.ModelSerializer):
    user_info = UserInfoSerializer(source='userinfo', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'user_info', 'email']