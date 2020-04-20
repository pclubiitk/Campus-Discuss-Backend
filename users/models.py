import string
import random
import secrets
from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    roll = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fblink = models.URLField(max_length=300,blank=True, null=True)
    following =models.ManyToManyField("self",symmetrical=False,blank=True, null=True) 
    password = models.CharField(max_length=70, null=True,blank=True)
    activated = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=70, blank=True, null=True)

    def generate_verification_code(self):
        # Generates verification code of length 28 made of digits and uppercase letters
        generated = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(28))
        self.verification_code = generated
        self.save()
        return self.verification_code

    def __str__(self):
        return self.name
