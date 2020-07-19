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
from .serializers import PostByStreamSerializer, StreamSerializer
from .utils import IsFollowing

class FollowStreamView(APIView):
    
    def put(self,request):
        user = IsLoggedIn(request)
        if user is not None:
            try:
                pk = request.data.get("pk")
                stream = Stream.objects.get(pk=pk)
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
                [k] = request.data.get("pk", "")
                if IsFollowing(user.username, pk) == False:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                stream = Stream.objects.get(pk=pk)
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
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class SubbedStreamsView(APIView):

    def get(self, request):
        try:
            user = IsLoggedIn(request)
            if user is None:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            streams = Stream.objects.filter(followed_by=user)
            serializer = StreamSerializer(streams, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except :
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AllStreamsView(APIView):

    def get(self, request):
        try:
            user = IsLoggedIn(request)
            if user is None:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            subbed_streams = Stream.objects.filter(followed_by=user)
            serializer = StreamSerializer(subbed_streams, many=True)
            subbed = serializer.data
            for stream in subbed:
                stream['is_subscribed']=True
            unsubbed_streams = Stream.objects.all().exclude(followed_by=user)
            serializer = StreamSerializer(unsubbed_streams, many=True)
            unsubbed = serializer.data
            for stream in unsubbed:
                stream['is_subscribed']=False

            data = unsubbed + subbed
            return Response(data, status=status.HTTP_200_OK)
        except :
            return Response(status=status.HTTP_400_BAD_REQUEST)
