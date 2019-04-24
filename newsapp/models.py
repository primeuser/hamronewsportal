from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Organization(models.Model):
    title = models.CharField(max_length=200)
    slogan = models.CharField(max_length=500)
    logo = models.ImageField(upload_to="organization")
    image = models.ImageField(upload_to="organization", null=True, blank=True)
    address = models.CharField(max_length=500)
    location = models.CharField(max_length=20)
    mission = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    mobile1 = models.CharField(max_length=20, null=True)
    mobile2 = models.CharField(max_length=20, null=True)
    email1 = models.EmailField()
    email2 = models.EmailField(null=True, blank=True)
    about = models.TextField()
    established = models.DateField()

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='post_photo', null=True)
    date_created = models.DateTimeField(default=timezone.now, blank=True)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(
        PostCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.author


class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.ImageField(
        upload_to='admin/', default="/default.jpg")
    about = models.TextField()

    def __str__(self):
        return self.user.username


class Editor(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.ImageField(upload_to='editor/',
                              default="/default.jpg")
    about = models.TextField()

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.ImageField(upload_to='subscribers/',
                              default="/default.jpg")

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.PROTECT, related_name="comments")
    comment = models.TextField()
    comment_by = models.ForeignKey(Subscriber, on_delete=models.PROTECT)

    def __str__(self):
        return self.comment


class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')

    def __str__(self):

        return self.title
