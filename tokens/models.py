from django.db import models
from users.models import User

# Create your models here.

class Tokens(models.Model):
    token = models.CharField(max_length=100, primary_key=True)
    user = models.ManyToManyField(User, related_name="token")
