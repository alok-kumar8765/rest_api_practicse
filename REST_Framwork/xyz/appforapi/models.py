from django.db import models

# Create your models here.
class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    descripion = models.TextField(blank=True,default='')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return self.name