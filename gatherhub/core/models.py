from django.db import models
from django.contrib.auth import get_user_model

class Conference(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=300)
    