from django.db import models
from users.models import User


class Post(models.Model):
	post_text  = models.CharField(max_length = 5000)
	post_title = models.CharField(max_length = 100)
	pub_date= models.DateTimeField('date field')
	author = models.ForeignKey(User , on_delete= models.CASCADE)
