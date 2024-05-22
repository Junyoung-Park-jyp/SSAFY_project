from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', user_profile, name='user-profile'),
    path('profile/update-profile/', update_user_profile, name='update-user-profile'),
    path('profile/update-info/', update_user_info, name='update-user-info'),
    path('userinfo/', user_info, name='user-info'),
    path('add-deposit/', add_deposit, name='add-deposit'),
    path('add-saving/', add_saving, name='add-saving')
]
    