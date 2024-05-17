from rest_framework import serializers
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'saving_products', 'deposit_products', 'bank', 'age', 'current_balance', 'annual_salary']


class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=False,)
    bank = serializers.CharField(max_length=20, required=True)
    email = serializers.EmailField(required=True)
    def get_cleaned_data(self):
        return {
        'username': self.validated_data.get('username', ''),
        'password1': self.validated_data.get('password1', ''),
        # age, bank 필드 추가
        'age': self.validated_data.get('age', ''),
        'bank': self.validated_data.get('bank', '')
        }
