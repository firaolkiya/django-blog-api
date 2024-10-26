from django.urls import path

from .views import SignUpView,LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('signup/', SignUpView.as_view(),name='signup'),
    path('login/', LoginView.as_view(),name='login'),
    path('jwt/create',TokenObtainPairView.as_view(),name = 'create'),
    path('jwt/refresh',TokenRefreshView.as_view(),name = 'refresh'),
    path('jwt/verify',TokenObtainPairView.as_view(),name = 'verify')



]
