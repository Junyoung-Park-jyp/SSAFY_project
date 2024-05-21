from django.db import models

class ExchangeRate(models.Model):
    currency = models.CharField(max_length=3, unique=True)
    rate = models.FloatField()
    country_name_ko = models.CharField(max_length=50)
    country_name_en = models.CharField(max_length=50)

    def __str__(self):
        return self.currency
