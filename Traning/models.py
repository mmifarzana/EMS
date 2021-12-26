from django.db import models
from django.utils.translation import gettext_lazy as _


class traning(models.Model):
        title = models.CharField(max_length=100)
        discription = models.TextField()
        img = models.ImageField(upload_to='images')
        date = models.DateField()
        action = models.CharField(max_length=100)
        


class Applying_traning(models.Model):
        
        class Status(models.TextChoices):
                CL = 'pending', _('Pending')
                SL = 'accepted', _('Accepted')
                YL = 'rejected', _('Rejected')
        Name = models.CharField(max_length=100)
        Possition = models.CharField(max_length=100)
        Course_name = models.CharField(max_length=100)
        Applying_date = models.DateField()
        Status = models.CharField(max_length=30, choices=Status.choices, default="pending")
        