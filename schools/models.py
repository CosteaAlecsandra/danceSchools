from django.db import models

# Create your models here.

class School(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
