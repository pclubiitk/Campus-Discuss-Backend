from django.db import models
from posts.models import Post
from duties.models import Duty

class Stream(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 1000)
    posts = models.ManyToManyField(Post, blank = True)
    #followed_by = models.ManyToManyField('users.User',through='duties.Duty', blank = True)
    followed_by = models.ManyToManyField('users.User', blank = True)

    def __str__(self):
        return self.title
