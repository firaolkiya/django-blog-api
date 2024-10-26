from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status,generics,mixins
from .serializers import PostSerializer
from .models import Post
from django.shortcuts import get_object_or_404
from account.permissions import AuthOrReadOnly


# @api_view(http_method_names=["GET"])
# def all_post(request:Request):
#     posts = Post.objects.all()
#     serializer = PostSerializer(instance = posts,many = True)
#     response = {
#         'message' : 'those are all post',
#         'data': serializer.data
#     }
#     return Response(data= response,status=status.HTTP_200_OK)


# @api_view(http_method_names=["POST"])
# def add_post(request:Request):
#     serializer = PostSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(http_method_names=['GET'])
# def get_post(request:Request, id:str):
#     post = Post.objects.filter(id=id).first()
#     if post:
#         serializer = PostSerializer(post)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)


# @api_view(http_method_names=["PUT"])
# def update_post(request:Request, id:str):
#     post = Post.objects.filter(id=id).first()
#     if post:
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

# @api_view(http_method_names=["GET"])
# def delete_post(request:Request,id:str):
#     post = Post.objects.filter(id=id).first()
#     if post:
#         post.delete()
#         return Response({'message': 'Post deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#     else:
#         return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)



class GetAllCreateView(APIView):
    
    serializer = PostSerializer
    permission_classes = [AuthOrReadOnly]
    def get(self,request:Request):
        posts = Post.objects.all()
        serializer = PostSerializer(instance = posts,many = True)
        response = {
            'message' : 'those are all post',
            'data': serializer.data
        }
        return Response(data= response,status=status.HTTP_200_OK)

    
    def post(self,request:Request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UDGview(APIView):
    
    serializer = PostSerializer
    permission_classes = [AuthOrReadOnly]
    def get(self,request:Request,id:str):
        post = Post.objects.filter(id=id).first()
        if post:
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)


    
    def put(self,request:Request,id:str):
        post = Post.objects.filter(id=id).first()
        if post:
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    
    def delete(self,request:Request,id:str):
        post = get_object_or_404(Post,id = id)
        # post = Post.objects.filter(id=id).first()
        if post:
            post.delete()
            return Response({'message': 'Post deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    
class ListPostForUser(
    generics.GenericAPIView,
    mixins.ListModelMixin):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
    
    def get(request, *args, **kwargs):
        return list(request,**args,**kwargs)