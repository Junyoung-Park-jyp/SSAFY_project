from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_pk>/comments/', views.comment_list, name='comment_list'),
    path('posts/<int:post_pk>/comments/<int:pk>/', views.comment_detail, name='comment_detail'),
]
