from django.urls import path
from .views import login_view, user_profile, update_user_profile, update_user_info, user_info

urlpatterns = [
    path('profile/', user_profile, name='user-profile'),
    path('profile/update-profile/', update_user_profile, name='update-user-profile'),
    path('profile/update-info/', update_user_info, name='update-user-info'),
    path('userinfo/', user_info, name='user-info'),
    path('auth/login/', login_view, name='login'),  # 로그인 엔드포인트 추가
]
