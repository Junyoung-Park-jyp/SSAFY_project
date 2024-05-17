from django.urls import path
from . import views

urlpatterns = [
    path('depositproducts/', views.depositproducts_list, name='depositproducts_list'),
    path('depositproducts/<int:pk>/', views.depositproduct_detail, name='depositproduct_detail'),
    path('savingproducts/', views.savingproducts_list, name='savingproducts_list'),
    path('savingproducts/<int:pk>/', views.savingproduct_detail, name='savingproduct_detail'),
]
