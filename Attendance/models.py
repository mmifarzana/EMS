from django.db import models


class attendance(models.Model):
        date = models.DateField()
        name = models.CharField(max_length=100)
        punch_in = models.CharField(max_length=100)
        punch_out = models.CharField(max_length=100)
        production = models.CharField(max_length=100)
        time_of_break = models.CharField(max_length=100)
        