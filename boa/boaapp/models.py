# boaapp/models.py

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Document(models.Model):
    uploaded_file = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class AudioFile(models.Model):
    title = models.CharField(max_length=100, default="Untitled")
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='audio/')
    metadata = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.title}"
