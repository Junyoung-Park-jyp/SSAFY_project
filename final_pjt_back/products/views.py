from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from django.http import JsonResponse

# Create your views here.
def get_er(request):
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=rhw2ldfOz9zngLX1vFIFFjwEUWwHBBWi&searchdate=20240516&data=AP01'
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data, safe=False)