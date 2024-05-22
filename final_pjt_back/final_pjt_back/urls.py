from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', include('products.urls')),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/community/', include('community.urls')),
    path('api/v1/exchange/', include('exchange.urls')),
    path('api/v1/banks/', include('banks.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    
]
