from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import SavingProducts, DepositProducts

class User(AbstractUser):
    pass






class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saving_products = models.ManyToManyField(SavingProducts, blank=True, related_name='users')
    deposit_products = models.ManyToManyField(DepositProducts, blank=True, related_name='users')
    bank = models.CharField(max_length=20)
    age = models.IntegerField(null=True, blank=True)
    current_balance = models.IntegerField(null=True, blank=True)
    annual_salary = models.IntegerField(null=True, blank=True)
