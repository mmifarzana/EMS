from django.db import models


class leave(models.Model):
        date = models.DateField()
        name = models.CharField(max_length=100)
        possition = models.CharField(max_length=100)
        leave_type = models.CharField(max_length=100)
        form =  models.DateField()
        to =  models.DateField()
        number_of_days = models.IntegerField()
        leave_reason = models.CharField(max_length=100)
        location_on_leave = models.CharField(max_length=100)
        action = models.CharField(max_length=100)
        
        
