from django import forms
from .models import *
  
class LeaveForm(forms.ModelForm):
  
    class Meta:
        model = Leave
        fields = "__all__"