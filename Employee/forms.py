from django import forms
from .models import *
  
class EmpolyeeForm(forms.ModelForm):
  
    class Meta:
        model = Empolyee
        fields = "__all__"