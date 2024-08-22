from django.db import models
from datetime import datetime

class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField(default=datetime.now)
    def __str__(self):
        return self.headline

