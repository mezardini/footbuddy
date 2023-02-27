from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=200)
    mod = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name[0:20]

class Topic(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    room =  models.ForeignKey(Room, on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
 
    def __str__(self):
        return self.body[0:100]


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
 
    def __str__(self):
        return self.body[0:50]







