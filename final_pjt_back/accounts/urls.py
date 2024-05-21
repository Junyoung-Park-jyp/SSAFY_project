from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', user_profile, name='user-profile'),
    path('profile/update-profile/', update_user_profile, name='update-user-profile'),
    path('profile/update-info/', update_user_info, name='update-user-info')
]
    