from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True,blank=True)
    work = models.CharField(max_length= 400)
    avatar = models.ImageField(upload_to="profile", default="avatar.svg")
    bio = models.TextField()

    def __str__(self):
        return self.username

class Topic(models.Model):
    name = models.CharField(max_length=300)
    info = models.CharField(max_length= 500, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    host = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    images = models.ImageField(upload_to="post_images", blank=True, null=True)
    description = models.TextField(null=True,blank=True)
    read = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def imageurl(self):
        if self.images:
            return self.images.url
        return ""

    class Meta:
        ordering = ["-created"]


    def __str__(self):
        return self.name
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]


    def __str__(self):
        return self.body[0:10]



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    messages = models.TextField(max_length=3000)

    def __str__(self):
        return self.email