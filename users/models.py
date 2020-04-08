from django.db import models
from django.contrib.postgres.fields import ArrayField
from streams.models import Stream
#from duties.models import duty
from posts.models import Post
from bookmark.models import Bookmark

class User(models.Model):
    roll = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fblink = models.URLField(max_length=300)
    posts = models.ManyToManyField(Post)
    streams = models.ManyToManyField(Stream)
    #moderating = models.ManyToManyField(Stream, through='duty', blank=True)
    bookmarks = models.ManyToManyField(Bookmark)
    following = ArrayField(models.IntegerField())

    def __str__(self):
        return self.name

