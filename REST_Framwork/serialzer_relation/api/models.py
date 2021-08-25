from django.db import models

# many to one relation.

class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    
    def __self__(self):
        return self.name

class Songs(models.Model):
    title = models.CharField(max_length=50)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE,related_name='song')
    duration = models.IntegerField()
    
    def __self__(self):
        return self.title