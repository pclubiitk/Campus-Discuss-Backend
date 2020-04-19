from django.db import models
class Stream(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 1000)
    followed_by = models.ManyToManyField('users.User', blank = True)

    def __str__(self):
        return self.title
