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

    def post(self,request,*args, **kwargs):
        user=IsLoggedIn(request)
        if user is not None :
            return Response(status=status.HTTP_400_BAD_REQUEST)

        username=request.data.get("username","")    

