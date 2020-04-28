from django.shortcuts import render
from users.utils import IsLoggedIn
from django.contrib.auth import login, logout
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import bcrypt
from rest_framework.decorators import api_view, renderer_classes
from .models import Post
from streams.models import Stream
from rest_framework.views import APIView
#@csrf_exempt

class CreatePostView(APIView):
    
    def post(self, request):
        try:
            user=IsLoggedIn(request)
            if user is None:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            post_text=request.data['post_text']
            post_title=request.data['post_title']
            stream_title=request.data['stream_title']
            try:
                stream = Stream.objects.get(title=stream_title)    
                Post.objects.create(post_title=post_title,post_text=post_text,author=user,stream=stream)
                return Response(status=status.HTTP_201_CREATED)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
