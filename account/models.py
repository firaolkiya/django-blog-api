from    django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email,password=None,**extra_fields):
        if not email:
            raise ValueError('User name cannot empty')
        
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)
    
    
class CustomUser(AbstractUser):
    email = models.CharField(max_length=80, unique = True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateTimeField(null=True)
    city = models.CharField(max_length=50)
    
    REQUIRED_FIELDS = ['city','username']
    
    USERNAME_FIELD = 'email'
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.username