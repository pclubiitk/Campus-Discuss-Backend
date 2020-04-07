from django.db import models
#from users.models import User
#from posts.models import Post
# Create your models here.

class Stream(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 1000)
    posts = models.ManyToManyField(Post, blank = True)
    followed_by = models.ManyToManyField(User, blank = True)

    def __str__(self):
        return self.title



