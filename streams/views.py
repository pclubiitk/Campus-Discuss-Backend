from django.shortcuts import render, redirect
from users.utils import IsLoggedIn
from django.contrib.auth import login, logout
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Stream
from users.models import User
from .serializers import PostByStreamSerializer
from .utils import IsFollowing

class FollowStreamView(APIView):
    
    def put(self,request):
        user = IsLoggedIn(request)
        if user is not None:
            try:
                stream_title = request.data.get("title")
                stream = Stream.objects.get(title=stream_title)
                stream.followed_by.add(user)
                stream.save()
                return Response(status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED) 

class UnfollowStreamView(APIView):

    def delete(self, request):
        user = IsLoggedIn(request)
        if user is not None:
            try:
                stream_title = request.data.get("title", "")
                if IsFollowing(user.username, stream_title) == False:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                stream = Stream.objects.get(title=stream_title)
                stream.followed_by.remove(user)
                return Response(status=status.HTTP_200_OK)

            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class PostsByStreamView(APIView):

    def get(self,request,pk):
        try:
            stream = Stream.objects.get(pk=pk)
            serializer = PostByStreamSerializer(stream)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
