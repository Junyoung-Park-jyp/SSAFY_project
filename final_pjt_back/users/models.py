from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    subscribed_products = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
