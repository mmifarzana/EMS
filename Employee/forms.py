from django import forms
from .models import *
  
class EmployeeForm(forms.ModelForm):
  
    class Meta:
        model = employee
        fields = "__all__"