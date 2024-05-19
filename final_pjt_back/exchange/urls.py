from django.urls import path
from . import views

urlpatterns = [
    path('rate/', views.get_exchange_rate, name='get_exchange_rate'),
]
