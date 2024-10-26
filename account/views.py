from django.shortcuts import render
from rest_framework import generics, status
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import AllowAny
from .serializers import SignupSerializer
from .tokens import get_token_for_user
# Create your views here.
class SignUpView(generics.GenericAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny] 
    
    def post(self,request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)   
        
        if serializer.is_valid():
            serializer.save()
            response = {
                'Message' : 'User created successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST )
    
    def get(self,request:Request):
        pass
    

class LoginView(APIView):
    
    # serializer = LoginSerailizer
    permission_classes = [AllowAny] 
    def post(self,request:Request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(email = email,password = password)
        if user is not None:
            response = {
                'message': "logged in successfully",
                "token": get_token_for_user(user)
            }
            return Response(response,status=status.HTTP_200_OK)
        return Response({'message':'invalid email or password'},status=status.HTTP_401_UNAUTHORIZED)
    
    def get(self,request:Request):
        content = {
            'user':str(request.user),
            'auth':str(request.auth)
        }
        return Response(content,status=status.HTTP_200_OK)