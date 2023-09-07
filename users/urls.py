from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from users.views import MyTokenObtainPairView
from django.urls import path

urlpatterns = [
    path('token',MyTokenObtainPairView.as_view(),name = 'token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name = 'token_refresh_view'),
]