from django.db import models
from users.models import User
from streams.models import Stream
# Create your models here.
class Duty(models.Model):
    users=models.ForeignKey(User,on_delete=models.CASCADE)
    streams=models.ForeignKey(Stream,on_delete=models.CASCADE)

