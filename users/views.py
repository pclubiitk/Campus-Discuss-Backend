from django.contrib.auth import login, logout
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from posts.models import Post
from posts.serializers import *
from .utils import *
from django.contrib.auth.hashers import check_password
from rest_framework.parsers import JSONParser
from campusdiscussbackend.settings_email import *
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.core.mail import *
from django.views.decorators.csrf import csrf_exempt
import bcrypt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from bookmark.models import Bookmark
from users.serializers import UserViewSerializer
# @csrf_exempt

class UserView(APIView):

    def get(self, request):
        try:
            user = IsLoggedIn(request)
            if user is None:
                return HttpResponse("User not logged in.",status=401)
            serializer = UserViewSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return HttpResponse("Bad Request.",status=400)

class RegistrationView(APIView):

    def post(self, request):
        if IsRegistered(request) is False:
            ActivationMailer(request)
            return Response(status = status.HTTP_202_ACCEPTED)
        if IsRegistered(request) is True:
            return Response(status = status.HTTP_403_FORBIDDEN)
        if IsRegistered(request) is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response(status = status.HTTP_400_BAD_REQUEST)

class ResetPassView(APIView):

    def post(self, request):
        if IsRegistered(request) is True:
            ResetPasswordEmail(request)
            return Response(status = status.HTTP_202_ACCEPTED)
        if IsRegistered(request) is False:
            return Response(status = status.HTTP_403_FORBIDDEN)
        if IsRegistered(request) is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response(status = status.HTTP_400_BAD_REQUEST)

#Create Forgot password API
class ForgotPassView(APIView):

    def post(self, request):
        if IsRegistered(request) is True:
            ForgotPassMailer(request)
            return Response(status = status.HTTP_202_ACCEPTED)
        if IsRegistered(request) is False:
            return Response(status = status.HTTP_403_FORBIDDEN)
        if IsRegistered(request) is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response(status = status.HTTP_400_BAD_REQUEST)
def ForgotPassMailer(request): 
    if request.method == "POST":
        try:
            roll_no = request.data['roll']
            user_data = User.objects.get(roll = roll_no)
            sender = EMAIL_HOST_USER
            recipient = user_data.email
            name = user_data.name
            user_code = user_data.generate_verification_code()
            user_link = EMAIL_LINK["ForgotPass"].format(code = user_code)
            subject = EMAIL_SUBJECT["ForgotPass"]
            body = EMAIL_BODY["ForgotPass"].format(name=name, link=user_link)
            send_mail(subject, body, sender, [recipient], fail_silently=False)
            return redirect(REDIRECT_LINK["ForgotPass"])
        except:
            return HttpResponse("Please set up email host details!", status=206)
    else :
        return HttpResponse("Invalid request!", status=400)
@api_view(['POST'])
def ForgotPass(request,token):
    if request.method == "POST":
        try:
            user_data=User.objects.get(verification_code=token)
            if user_data.activated==True:
                user_data.activated=False
                user_data.save()
                response={
                    'status':'success',
                    'code':status.HTTP_200_OK,
                    'message':'Account successfully deactivated. Now follow activation process to create new password and activate account',                }
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

#

#Create update fblink API
class FbLinkView(APIView):

    def post(self, request):
        user = IsLoggedIn(request)
        if user is not None:
            try:
                fb_link = request.data.get("fblink", "")
                user.fblink=fb_link
                user.save()
                return Response(status = status.HTTP_200_OK)
            
            except:
                return Response(status = status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
#

#Create Friend's profile(by name) API
class PeopleProfileViewName(APIView):

    def post(self,request):
        try:
            username = request.data.get("username", "")
            user = User.objects.get(username=username)
            if user is None:
                return HttpResponse("User does not exist.",status=401)
            serializer = UserViewSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return HttpResponse("Bad Request.",status=400)
# 
#Create Friend's profile(by roll) API
class PeopleProfileViewRoll(APIView):

    def post(self,request):
        try:
            roll_no = request.data.get("roll", "")
            user = User.objects.get(roll=roll_no)
            if user is None:
                return HttpResponse("User does not exist.",status=401)
            serializer = UserViewSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return HttpResponse("Bad Request.",status=400)
# 
class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        user = IsLoggedIn(request)
        if user is not None :
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        '''
        ###
        request.session["username"] = username 
        request.session.modified = True
        return Response(status = status.HTTP_200_OK)
        ###
        '''
        #encode converts a str type to byte type
        #when storing in database we decode() it to str type then store in charfield
        #any bcrypt function accepts only byte type 
        try:
            user = User.objects.get(username = username, activated = True)
            if user is not None:
                if bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
                    request.session["username"] = username 
                    request.session.modified = True
                    return Response(status = status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_401_UNAUTHORIZED)
            
        except :
            return Response(status = status.HTTP_401_UNAUTHORIZED)
        
    def get(self, request):
        if IsLoggedIn(request) is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status = status.HTTP_200_OK)

class LogoutView(APIView):

    def post(self, request):
        if IsLoggedIn(request) is not None:
            del request.session["username"]
            return Response(status = status.HTTP_200_OK)
        return Response(status = status.HTTP_401_UNAUTHORIZED)

class FollowUserView(APIView):

    def put(self, request):
        user = IsLoggedIn(request)
        if user is not None:
            username = request.data.get("username", "")
            if username == request.session["username"] or IsFollowing(request.session["username"], username):
                return Response(status = status.HTTP_400_BAD_REQUEST)
            try:
                follow_user = User.objects.get(username=username)
                user.following.add(follow_user)
                user.save()
                follow_user.save()
                return Response(status = status.HTTP_200_OK)
            
            except:
                return Response(status = status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class UnfollowUserView(APIView):

    def post(self, request):
        user = IsLoggedIn(request)
        if user is not None:
            username = request.data.get("username", "")
            try:
                if IsFollowing(request.session["username"], username):
                    unfollow_user = user.following.get(username=username)
                    user.following.remove(unfollow_user)
                    return Response(status = status.HTTP_200_OK)
                    
                else:
                    return Response(status = status.HTTP_400_BAD_REQUEST)

            except:
                return Response(status = status.HTTP_400_BAD_REQUEST)

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class UserFeedView(APIView):

    def get(self, request):
        user = IsLoggedIn(request)
        if user is not None:
            feed_posts_ids = list()
            posts = Post.objects.all()
            for post in posts:
                if user in post.stream.followed_by.all():
                    feed_posts_ids.append(post.id)
                elif post.author in user.following.all():
                    feed_posts_ids.append(post.id)
            feed_posts = Post.objects.filter(id__in=feed_posts_ids)
            serializer = PostSerializer(feed_posts, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

def ActivationMailer(request): 
    if request.method == "POST":
        try:
            roll_no = request.data['roll']
            user_data = User.objects.get(roll = roll_no)
            sender = EMAIL_HOST_USER
            recipient = user_data.email
            name = user_data.name
            user_code = user_data.generate_verification_code()
            user_link = EMAIL_LINK["Activation"].format(code = user_code)
            subject = EMAIL_SUBJECT["Activation"]
            body = EMAIL_BODY["Activation"].format(name=name, link=user_link)
            send_mail(subject, body, sender, [recipient], fail_silently=False)
            return redirect(REDIRECT_LINK["Activation"])
        except:
            return HttpResponse("Please set up email host details!", status=206)
    else :
        return HttpResponse("Invalid request!", status=400)

def HashPass(password):
    password=password.encode('utf-8')
    return bcrypt.hashpw(password,bcrypt.gensalt())

# @csrf_exempt
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


# @csrf_exempt
def ResetPasswordEmail(request):
    if request.method == "POST":
        try:
            roll_no = request.data['roll']
            user_data = User.objects.get(roll = roll_no)
            sender = EMAIL_HOST_USER
            recipient = user_data.email
            name = user_data.name
            user_code = user_data.generate_verification_code()
            user_link = EMAIL_LINK["PasswordReset"].format(code = user_code)
            subject = EMAIL_SUBJECT["PasswordReset"]
            body = EMAIL_BODY["PasswordReset"].format(name=name, link=user_link)
            send_mail(subject, body, sender, [recipient], fail_silently=False)
            return redirect(REDIRECT_LINK["PasswordReset"])
        except:
            return HttpResponse("Please set up email host details!", status=206)
    else :
        return HttpResponse("Invalid request!", status=400)

def pass_checker(old,password):
    return bcrypt.checkpw(old.encode("utf-8"),password)

# @csrf_exempt
@api_view(['POST'])
def ResetPassword(request,token):
    if request.method == "POST":
        try:
            new1=request.data['new_password1']
            new2=request.data['new_password2']
            old=request.data['old_password']
            user_data=User.objects.get(verification_code=token)
            password=(user_data.password)
            password=password.encode("utf-8")
            if user_data.activated==True:
                if(new1==new2):
                    if(pass_checker(old,password)==True):
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

class PostsByUserView(APIView):
    def get(self,request,pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = PostByUserSerializer(user)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PostsByBookmarksView(APIView):

    def get(self, request):
        user=IsLoggedIn(request)
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        bookmarks=Bookmark.objects.filter(user=user)
        posts=list()
        try:
            for bookmark in bookmarks:
                posts.append(bookmark.post)
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

