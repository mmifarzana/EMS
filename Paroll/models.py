from django.db import models


class paroll(models.Model):
        date = models.DateField()
        name = models.CharField(max_length=100)
        possition = models.CharField(max_length=100)
        salary = models.CharField(max_length=100)
        absent = models.CharField(max_length=100)
        total_salary = models.CharField(max_length=100)
        action = models.CharField(max_length=100)
        