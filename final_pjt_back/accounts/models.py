from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import SavingProducts, DepositProducts

# Create your models here.
class User(AbstractUser):
    saving_products = models.ManyToManyField(SavingProducts, blank=True, related_name='users')
    deposit_products = models.ManyToManyField(DepositProducts, blank=True, related_name='users')
    bank = models.CharField(max_length=20)
    age = models.IntegerField(null=True, blank=True, default=20)
    email = models.EmailField(max_length=254)
    current_balance = models.IntegerField(null=True, blank=True)
    annual_salary = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=20)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username'], name='unique_username')
        ]