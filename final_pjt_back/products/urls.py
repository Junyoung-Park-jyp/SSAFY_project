from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('er/', views.get_er)
]