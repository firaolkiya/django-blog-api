from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import *

class SignupSerializer(serializers.Serializer):
    email = serializers.CharField(max_length = 80)
    username = serializers.CharField(max_length = 50)
    password = serializers.CharField(min_length = 8,write_only = True)
    city = serializers.CharField(max_length = 50)
    class meta:
        model = CustomUser
        fields = ['email','password','username','city']
    
    def validate(self, attrs):
        is_eamil_exist = CustomUser.objects.filter(email = attrs['email']).exists()
        
        if is_eamil_exist:
            raise ValidationError('Email already exists')
        return super().validate(attrs)
    
    def create(self, validated_data):
        password =validated_data.pop('password')
        user = CustomUser.objects.create_user(**validated_data)
        
        user.set_password(password)
        user.save()
        Token.objects.create(user = user)
        
        return user 
    
    
# class LoginSerailizer(serializers.Serializer):
    
#     class meta:
#         models = CustomUser
#         fields = ['email','password']