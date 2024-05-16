from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import *

# Create your models here.
class User(AbstractUser):
    saving_products = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    deposit_products = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    bank = models.CharField(max_length=20)
    age = models.IntegerField()