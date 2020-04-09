from django.db import models
from django.contrib.postgres.fields import ArrayField
from streams.models import Stream
from duties.models import Duty
from posts.models import Post
from bookmark.models import Bookmark

class User(models.Model):
    roll = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fblink = models.URLField(max_length=300,blank=True, null=True)
    posts = models.ManyToManyField(Post,null=True,blank=True)
    streams = models.ManyToManyField(Stream,through='duties.Duty',blank=True, null=True)
    following =models.ManyToManyField("self",symmetrical=False,blank=True, null=True) 
    bookmarks = models.ManyToManyField(Bookmark,blank=True, null=True)
    def __str__(self):
        return self.name

