from django.db import models


class Post(models.Model):
	post_text  = models.CharField(max_length = 5000,null=True,blank=True)
	post_title = models.CharField(max_length = 100,null=True,blank=True)
	pub_date= models.DateTimeField('date field')
	author = models.ForeignKey('users.User' , on_delete= models.CASCADE)

	def __str__(self):
		return self.post_title
