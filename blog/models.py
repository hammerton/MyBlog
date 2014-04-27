from django.db import models

# Create your models here.
class BlogPosts(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    date = models.DateTimeField()
    textbody = models.TextField()