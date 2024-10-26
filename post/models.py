from django.db import models
from django.core.validators import MinLengthValidator

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=100)
    id = models.CharField(max_length=100, 
                          validators=[MinLengthValidator(50)],
                          primary_key=True,auto_created=True,blank=False,)
    
    def __str__(self):
        return self.title
