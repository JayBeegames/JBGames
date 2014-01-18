from django.db import models

# Create your models here.

class News(models.Model):

    title = models.CharField(max_length=40)
    message= models.CharField(max_length=200)
    author=models.CharField(max_length=40)
    bodytext= models.TextField()
    niggertext=models.TextField()

class posts(models.Model):

    author = models.CharField(max_length=30)
    title  = models.CharField(max_length=100)
    bodytext= models.TextField()
    timestamp= models.DateTimeField()
