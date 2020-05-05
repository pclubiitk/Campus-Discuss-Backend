from django.shortcuts import render
from users.utils import IsLoggedIn
from streams.utils import IsFollowing
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
from .serializers import PostSerializer

class CreatePostView(APIView):

    def post(self, request):
        try:
            user = IsLoggedIn(request)
            if user is None:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            post_text = request.data.get("text", "")
            post_title = request.data.get("title", "")
            stream_title = request.data.get("stream", "")
            stream = Stream.objects.get(title=stream_title)
            follow_stream = IsFollowing(request.session["username"], stream_title)
            if follow_stream == False:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            Post.objects.create(post_title=post_title, post_text=post_text, author=user, stream=stream)
            return Response(status=status.HTTP_201_CREATED)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class DeletePostView(APIView):

    def delete(self, request):
        user = IsLoggedIn(request)
        if user is not None:
            try:
                pk = request.data.get("pk", "")
                post = Post.objects.get(pk=pk)
                author = post.author
                if author == user:
                    post.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            except:
                return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class PostDetailView(APIView):

    def get(self, request):
        pk = request.data.get("pk", "")
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class EditPostView(APIView):

    def put(self, request):
        user = IsLoggedIn(request)
        if user is not None:
            try:
                pk = request.data.get("pk", "")
                post = Post.objects.get(pk=pk)
                author = post.author
                print(post.pub_date, post.last_modified, sep='\n')
                if author == user:
                    post_text = request.data.get("text", "")
                    post_title = request.data.get("title", "")
                    post.post_title = post_title
                    post.post_text = post_text
                    post.save()
                    print(post.pub_date, post.last_modified, sep='\n')
                    return Response(status=status.HTTP_201_CREATED)
                
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)

            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
