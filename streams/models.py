from django.db import models
from users.models import User
from posts.models import Posts
# Create your models here.

class Stream(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 1000)
    posts = models.ManyToManyField(Posts, blank = True)
    followed_by = models.ManyToManyField(User, blank = True)
    follower_number = models.IntegerField()

    def __str__(self):
        return self.title



