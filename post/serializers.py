from rest_framework import serializers
from .models import Post

# Create a serializer class for the Post model.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'owner', 'title', 'content', 'created_at', 'updated_at')