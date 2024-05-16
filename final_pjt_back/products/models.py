from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    interest_rate = models.FloatField()
    duration_months = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
