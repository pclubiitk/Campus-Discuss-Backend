from django.db import models
from users.models import User

# Create your models here.

class Tokens(models.Model):
    token = model.CharField(primary_key=True)
    user = model.ManyToManyField(User, related_name="token")
