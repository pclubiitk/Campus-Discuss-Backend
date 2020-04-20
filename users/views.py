from django.shortcuts import render
from django.contrib.auth import login,logout
from rest_framework import permissions,status
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
from campusdiscussbackend.settings_email import *
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
# @csrf_exempt

class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        user_data = IsLoggedIn(request)
        if user_data is not None :
            return Response(status = status.HTTP_400_BAD_REQUEST)
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        
        try:
            user_data = User.objects.get(username = username, activated = True)
            if user_data is not None:
                if bcrypt.checkpw(password, user_data.password):
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




@csrf_exempt
def ActivationMailer(request): 
    if request.method == "POST":
        try:
            roll_no = JSONParser().parse(request)
            user_data = User.objects.get(roll = roll_no['roll'])
            sender = EMAIL_HOST_USER
            recipient = user_data.email
            name = user_data.name
            user_code = user_data.generate_verification_code()
            user_link = ACTIVATION_LINK[0].format(code = user_code)
            subject = ACTIVATION_SUBJECT[0]
            body = ACTIVATION_BODY[0].format(name=name, link=user_link)
            send_mail(subject, body, sender, [recipient], fail_silently=False)
            return redirect(ACTIVATION_REDIRECT[0])
        except:
            return HttpResponse("Please set up email host details!", status=206)
    else :
        return HttpResponse("Invalid request!", status=400)




def HashPass(password):
    password=password.encode()
    return bcrypt.hashpw(password,bcrypt.gensalt())




@csrf_exempt
@api_view(['POST'])
def SetPasswordAndActivate(request,token):
    if request.method == "POST":
        try:
            pw=request.data['password']
            user_data=User.objects.get(verification_code=token)
            if user_data.activated==False:
                user_data.activated=True
                user_data.password=HashPass(pw).decode()
                user_data.save()
                response={
                    'status':'success',
                    'code':status.HTTP_200_OK,
                    'message':'Password set succesfully and now you are registered',
                }
                return Response(response)
            else:
                response={
                'code':'status.HTTP_401_UNAUTHORIZED',
                'message':'Token already used'}
                return Response(response,status=401)  
        except:
            response={
                    'code':'status.HTTP_401_UNAUTHORIZED',
                    'message':'Invalid token or invalid request'
                }
            return Response(response,status=status.HTTP_401_UNAUTHORIZED)
    else:
        return HttpResponse("Invalid Request",status=400)





@csrf_exempt
def ResetPasswordEmail(request):
    if request.method == "POST":
        try:
            roll_no = JSONParser().parse(request)
            user_data = User.objects.get(roll = roll_no['roll'])
            sender = EMAIL_HOST_USER
            recipient = user_data.email
            name = user_data.name
            user_code = user_data.generate_verification_code()
            user_link = ACTIVATION_LINK[1].format(code = user_code)
            subject = ACTIVATION_SUBJECT[1]
            body = ACTIVATION_BODY[1].format(name=name, link=user_link)
            send_mail(subject, body, sender, [recipient], fail_silently=False)
            return redirect(ACTIVATION_REDIRECT[1])
        except:
            return HttpResponse("Please set up email host details!", status=206)
    else :
        return HttpResponse("Invalid request!", status=400)



def pass_checker(old,password):
    return bcrypt.checkpw(old.encode(),password)


@csrf_exempt
@api_view(['POST'])
def ResetPassword(request,token):
    if request.method == "POST":
        try:
            new1=request.data['new_password1']
            new2=request.data['new_password2']
            old=request.data['old_password']
            user_data=User.objects.get(verification_code=token)
            password=(user_data.password)
            print(type(password),"\n",password)
            password=password.encode()
            print(type(password),"\n",password)

            print(pass_checker(old,password))
            if user_data.activated==True:
                if(new1==new2):
                    print("yo\n")
                    print(pass_checker(old,password))
                    if(pass_checker(old,password)==True):
                        print("yo")
                        print(user_data.password)
                        user_data.password=HashPass(new1).decode()
                        user_data.save()
                        response={
                            'status':'success',
                            'code':status.HTTP_200_OK,
                            'message':'Password reset succesfull and now you can login',
                        }
                        return Response(response)
                    else:
                        response={
                            'status':'failure',
                            'code':status.HTTP_401_UNAUTHORIZED,
                            'message':'wrong old password',
                        }
                        return Response(response)
                else:
                    response={
                        'status':'failure',
                        'code':401,
                        'message':"the retyped password doesn't match",
                    }
                    return Response(response)

            else:
                response={
                'code':'status.HTTP_401_UNAUTHORIZED',
                'message':'Unauthorised user or Account not activated'}
                return Response(response,status=401)  
        except:
            response={
                    'code':'status.HTTP_401_UNAUTHORIZED',
                    'message':'Invalid token or invalid request'
                }
            return Response(response,status=status.HTTP_401_UNAUTHORIZED)
    else:
        return HttpResponse("Invalid Request",status=400)


        