from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import *
from .models import ActivationMailer
from campusdiscussbackend.settings_email import *
# @csrf_exempt 
# Do not use until you want it to POST

# Create your views here.
'''
The send_email function is an API for sending any email.
In place of email_class, you can type in the class of email-type as
mentioned in settings_email.py. An example class is given as ExampleEmail
'''
def send_email(request, email_class): 
    if request.method == "POST":
        email_id = JSONParser().parse(request)
        serializer = Mailer(email_id)
        subject = email_class.EMAIL_SUBJECT
        body = email_class.EMAIL_BODY
        sender = EMAIL_HOST_USER
        recipient = serializer.data['email']
        send_email(subject, body, sender, [recipient], fail_silently=False)
        return redirect(email_class.REDIRECT_URL)
    else :
        return HttpResponse("Invalid request!", status=400)
