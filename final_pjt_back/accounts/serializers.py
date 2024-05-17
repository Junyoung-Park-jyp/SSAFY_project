from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'saving_products', 'deposit_products', 'bank', 'age', 'current_balance', 'annual_salary']

