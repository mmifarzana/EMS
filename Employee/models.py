from django.db import models


class emplyee(models.Model):
        name = models.CharField(max_length=100)
        img = models.ImageField(upload_to='images')
        Employee_id  = models.CharField(max_length=100)
        possition = models.CharField(max_length=100)
        salary = models.CharField(max_length=100)
        joining_date = models.DateField()
        phone = models.CharField(max_length=100)
        email = models.EmailField()
        birthday = models.DateField()
        address = models.CharField(max_length=100)
        nationality = models.CharField(max_length=100)
        religion = models.CharField(max_length=100)
        marital_statas = models.CharField(max_length=100)
        emergency_contact_name = models.CharField(max_length=100)
        relationship = models.CharField(max_length=100)
        emergency_contact_phone = models.CharField(max_length=100)
        
        
    
