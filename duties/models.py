from django.db import models

# Create your models here.
class Moderators(models.Model):
    moderator=models.ForeignKey('users.User')
    streams=models.ManyToManyField('streams.Streams')
    #powers=models.ForeignKey('powers.Powers')

