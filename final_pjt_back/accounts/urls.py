from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', user_profile, name='user-profile'),
    path('profile/update/', update_user_profile, name='update-user-profile'),
    path('userinfo/', user_info, name='user-info')
]
    