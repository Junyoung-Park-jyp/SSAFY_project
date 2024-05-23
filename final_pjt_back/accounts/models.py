from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import *

class User(AbstractUser):
    pass






class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saving_options = models.ManyToManyField(SavingOptions, blank=True, related_name='users')
    deposit_options = models.ManyToManyField(DepositOptions, blank=True, related_name='users')
    bank = models.CharField(max_length=20)
    age = models.IntegerField(null=True, blank=True, default=20)
    current_balance = models.IntegerField(null=True, blank=True)
    annual_salary = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=20)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username'], name='unique_username')
        ]

