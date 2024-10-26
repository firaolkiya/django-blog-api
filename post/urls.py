from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", GetAllCreateView.as_view(), name='home'),
    path('<str:id>/', UDGview.as_view(),name='get_post'),
    path('postuser/',ListPostForUser.as_view(),name='listforcurrentuser')
   
]
