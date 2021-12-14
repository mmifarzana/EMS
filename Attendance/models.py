from django.db import models


class attendance(models.Model):
        date = models.DateField()
        name = models.CharField(max_length=100)
        punch_in = models.DateTimeField()
        punch_out = models.DateTimeField()
        production = models.IntegerField()
        time_of_break = models.IntegerField()
        