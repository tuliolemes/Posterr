from django.shortcuts import render
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import viewsets

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #http_method_names = ['get', 'post', 'head']
    #permission_classes = [permissions.IsAuthenticated]