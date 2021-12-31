from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class Circular(models.Model):
    circular_No = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField( max_length=50)
    job_title = models.CharField( max_length=50)
    field = models.CharField( max_length=50)
    job_type = models.CharField( max_length=50)
    requirement = models.CharField( max_length=500)
    exprience =   models.CharField( max_length=500)
    email = models.EmailField( max_length=254)
    last_date_apply = models.DateField( auto_now_add=False)
    action = models.CharField( max_length=50)

    def __str__(self):
        return self.job_title

class Applyparticipent(models.Model):
    circular_No = models.IntegerField()
    full_name = models.CharField( max_length=50)
    job_title = models.CharField( max_length=50)
    job_type = models.CharField( max_length=50)
    field = models.CharField( max_length=50)
    related_exprience = models.CharField( max_length=500)
    job_reason =   models.CharField( max_length=500)
    email = models.EmailField( max_length=254)
    phone_no = models.CharField( max_length=50)
    image = models.ImageField(upload_to="participent_profiles/")
    cv = models.FileField(upload_to="participent_cv/")
    submission_date = models.DateTimeField(auto_now_add=True)
    action = models.CharField( max_length=50, null=True)
 
    def __str__(self):
        return self.job_title

