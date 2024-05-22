from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import *


class SavingProduct(models.Model):
    name = models.CharField(max_length=100)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    bank = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class DepositProduct(models.Model):
    name = models.CharField(max_length=100)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    bank = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    age = models.IntegerField()
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)
    annual_salary = models.DecimalField(max_digits=10, decimal_places=2)
    saving_preference = models.CharField(max_length=100)
    favorite_bank = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s Portfolio"

