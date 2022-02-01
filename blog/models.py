from turtle import title
from django.db import models
from django.contrib.auth.models import User

STATUS = ((0,'Draft'),(1,'Publish'))
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created =models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200,unique=True)
    #If a user is deleted form the user table, their posts will also be deleted through CASCADE
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    #define slef referencing method that returns title a string in the admin interface
    def __str__(self):
        return self.title