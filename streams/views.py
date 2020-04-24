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

@csrf_exempt
@api_view(['PUT'])
def FollowStreamAPI(request):
    if request.method == 'PUT':
        user = IsLoggedIn(request)
        if user is not None:
            request.session["username"] = user.username
            try:
                stream = Stream.objects.get(title = request.data.get("title"))
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            if stream is not None:
                stream.followed_by.add(user)
                stream.save()
                user.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED) 

