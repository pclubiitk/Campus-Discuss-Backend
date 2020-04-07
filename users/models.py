from django.db import models
from django.contrib.postgres.fields import ArrayField
#from streams.models import stream
#from duties.models import duty
#from posts.models import post

class User(models.Model):
    roll = models.CharField(maxlength=20, unique=True)
    username = models.CharField(maxlength=20)
    name = models.CharField(maxlength=100)
    email = models.CharField(maxlength=100)
    fblink = models.URLField(maxlength=300)
    #posts = models.ManyToManyField(post)
    #streams = models.ManyToManyField(stream)
    #moderating = models.ManyToManyField(stream, through='duty', blank=True)
    #bookmarks = models.ManyToManyField(bookmark)
    #following = ArrayField(models.IntegerField())