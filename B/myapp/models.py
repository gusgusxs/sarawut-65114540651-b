from django.db import models

# Create your models here.

class coruse (models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    name = models.IntegerField(max_length=100)
    info = models.IntegerField(max_length=100)
