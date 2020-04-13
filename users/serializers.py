from rest_framework import serializers
from .models import User
from django.core import mail

class ActivationMailer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['email'] # Can edit this according to data required