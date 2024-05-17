from django.urls import path
from .views import user_profile, update_user_profile

urlpatterns = [
    path('profile/', user_profile, name='user-profile'),
    path('profile/update/', update_user_profile, name='update-user-profile'),
]
