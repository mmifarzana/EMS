from django.db import models


class traning(models.Model):
        title = models.CharField(max_length=100)
        discription = models.TextField()
        img = models.ImageField(upload_to='images')
        date = models.DateField()
        action = models.CharField(max_length=100)
        
