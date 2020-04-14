from rest_framework import serializers
from .models import User
from django.core import mail

class Mailer(serializers.ModelSerializer):
    class Meta:
        model = User # Change this model according to requirement
        fields=['email'] # Can edit this according to data required