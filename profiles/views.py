import re
from django.shortcuts import render
from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


    @action(detail=True)
    def recent_posts(self, request, pk):
        pass
        # profile = Profile.objects.get(user=request.user)
        # recent_posts = profile.profiles_posts()
        # page = self.paginate_queryset(recent_posts)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        # serializer = self.get_serializer(recent_posts, many=True)
        # return Response(serializer.data)
