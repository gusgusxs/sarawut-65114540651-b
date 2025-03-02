from django.db import models

# Create your models here.

class coruse (models.Model):
    coruseid = models.IntegerField(unique=True,primary_key=True)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.coruseid},{self.name},{self.info}"