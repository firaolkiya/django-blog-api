from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

CustomUser =  get_user_model()

def get_token_for_user(user):
    refresh_token = RefreshToken.for_user(user)
    token =  {
         'refresh':str(refresh_token),
         'access' : str(refresh_token.access_token)
        }
    return token