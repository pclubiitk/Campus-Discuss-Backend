from django.db import models
import datetime
from posts.models import Post

class Bookmark(models.Model):

    date_created = models.DateField(auto_now_add=True)
    #user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.OneToOneField(Post, on_delete=models.CASCADE,blank=True, null=True)


    def __str__(self):
        return f'Bookmark created at {self.date_created} '

