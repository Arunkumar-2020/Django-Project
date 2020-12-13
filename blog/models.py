from django.db import models
from datetime import datetime


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(default=datetime.now())
    author = models.CharField(max_length=40)
    image = models.ImageField(upload_to='blog/static/blog/images/', blank=True)

    def __str__(self):
        return self.title
