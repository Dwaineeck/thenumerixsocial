# models.py

from django.db import models


class Notebook(models.Model):
    title = models.CharField(max_length=200)
    file_path = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Section(models.Model):
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f"{self.notebook.title} - {self.title}"

class AudioFile(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=500)
    duration = models.DurationField()

    def __str__(self):
        return self.file_path

class Video(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=500)
    duration = models.DurationField()

    def __str__(self):
        return self.file_path
