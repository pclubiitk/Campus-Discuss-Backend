from django.db import models
from django.contrib.postgres.fields import ArrayField
#from streams.models import stream
#from duties.models import duty
#from posts.models import post

class User(models.Model):
    roll = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fblink = models.URLField(max_length=300)
    #posts = models.ManyToManyField(post)
    #streams = models.ManyToManyField(stream)
    #moderating = models.ManyToManyField(stream, through='duty', blank=True)
    #bookmarks = models.ManyToManyField(bookmark)
    #following = ArrayField(models.IntegerField())

    def __str__(self):
        return self.name

