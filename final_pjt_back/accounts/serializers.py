from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'saving_products', 'deposit_products', 'bank', 'age', 'current_balance', 'annual_salary']


class CustomRegisterSerializer(RegisterSerializer):
    # 필요한 필드들을 추가합니다.
    age = serializers.IntegerField(
        required=False,
        )
    bank = serializers.CharField(
        max_length=20,
        required=True
    )
    # 해당 필드도 저장 시 함께 사용하도록 설정합니다.
    def get_cleaned_data(self):
        return {
        'username': self.validated_data.get('username', ''),
        'password1': self.validated_data.get('password1', ''),
        # nickname 필드 추가
        'nickname': self.validated_data.get('nickname', ''),
        }
