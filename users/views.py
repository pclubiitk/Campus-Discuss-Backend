from django.shortcuts import render
from django.contrib.auth import login,logout
from rest_framework import permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .utils import IsLoggedIn
import bcrypt
from django.contrib.auth.hashers import check_password

class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        user = IsLoggedIn(request)
        if user is not None :
            return Response(status = status.HTTP_400_BAD_REQUEST)
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        
        try:
            user = User.objects.get(username = username, activated = True)
            if user is not None:
                if bcrypt.checkpw(password, user.password):
                        request.session["username"] = username 
                        request.session.modified = True                     
                        return Response(status = status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_401_UNAUTHORIZED)
            
        except :
            return Response(status = status.HTTP_401_UNAUTHORIZED)
        
    def get(self, request):
        if IsLoggedIn(request) is not None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status = status.HTTP_200_OK)

class LogoutView(APIView):

    def post(self, request):
        if IsLoggedIn(request) is not None:
            del request.session["username"]
            return Response(status = status.HTTP_200_OK)
        return Response(status = status.HTTP_401_UNAUTHORIZED)


