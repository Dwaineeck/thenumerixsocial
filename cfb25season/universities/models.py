# universities/models.py
from django.db import models


class University(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    logo_url = models.URLField()
    schedule = models.JSONField(default=dict)  # To store the schedule
    recent_game = models.JSONField(default=dict)  # To store recent game info
    stats = models.JSONField(default=dict)  # To store stats

    def __str__(self):
        return self.name
