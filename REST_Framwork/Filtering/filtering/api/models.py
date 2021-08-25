from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    roll = models.IntegerField()
    passby = models.CharField(max_length=50)