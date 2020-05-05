from django.db import models


class Post(models.Model):
	post_text  = models.CharField(max_length = 5000, null=True, blank=True)
	post_title = models.CharField(max_length = 100, null=True, blank=True)
	pub_date = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	author = models.ForeignKey('users.User', on_delete= models.CASCADE)
	stream = models.ForeignKey('streams.Stream', default=None, on_delete=models.CASCADE, db_column="title")

	class Meta:
		ordering = ['-pub_date']

	def __str__(self):
		return f'#{self.pk}'
