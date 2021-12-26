from django.db import models
from django.utils.translation import gettext_lazy as _


class Leave(models.Model):
        class LeaveType(models.TextChoices):
                CL = 'casual_leave', _('Casual Leave')
                SL = 'sick_leave', _('Sick Leave')
                YL = 'yearly_leave', _('Yearly Leave')

        class LeaveStatus(models.TextChoices):
                CL = 'pending', _('Pending')
                SL = 'accepted', _('Accepted')
                YL = 'rejected', _('Rejected')
        date = models.DateField()
        name = models.CharField(max_length=100)
        possition = models.CharField(max_length=100)
        leave_type = models.CharField(max_length=30, choices=LeaveType.choices)
        form =  models.DateField()
        to =  models.DateField()
        number_of_days = models.IntegerField()
        leave_reason = models.CharField(max_length=100)
        location_on_leave = models.CharField(max_length=100)
        leave_status = models.CharField(max_length=30, choices=LeaveStatus.choices, default="pending")
        #action = models.CharField(max_length=100)
        
        
