from django.contrib.auth import login, logout
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .utils import IsLoggedIn
from django.contrib.auth.hashers import check_password
from rest_framework.parsers import JSONParser
from campusdiscussbackend.settings_email import *
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.core.mail import *
from django.views.decorators.csrf import csrf_exempt
import bcrypt
# @csrf_exempt

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


def ActivationMailer(request): 
    if request.method == "POST":
        roll_no = JSONParser().parse(request)
        user_data = User.objects.get(roll = roll_no['roll'])
        sender = EMAIL_HOST_USER
        recipient = user_data.email
        name = user_data.name
        user_code = user_data.generate_verification_code()
        user_link = ACTIVATION_LINK.format(code = user_code)
        subject = ACTIVATION_SUBJECT
        body = ACTIVATION_BODY.format(name=name, link=user_link)
        send_mail(subject, body, sender, [recipient], fail_silently=False)
        return redirect(ACTIVATION_REDIRECT)
    else :
        return HttpResponse("Invalid request!", status=400)
