from django.db import models
import datetime
class Bookmark(models.Model):

    date_created = models.DateField("Created time")

    def __str__(self):
        return

