from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import *
from .models import ActivationMailer
from campusdiscussbackend.settings import EMAIL_HOST_USER
# @csrf_exempt 
# Do not use until you want it to POST

# Create your views here.

def send_email(request):
    if request.method == "POST":
        emailid=JSONParser().parse(request)
        serialiser=ActivationMailer(emailid)
        subject="Activation mail"
        body="Body"
        recepient=serialiser.data['email']
        send_email(subject, body, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return redirect("https://redirect.link")
    else :
        return HttpResponse("Invalid request!", status=400)
