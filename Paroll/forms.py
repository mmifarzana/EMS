from django import forms
from .models import *
  
class ParollForm(forms.ModelForm):
  
    class Meta:
        model = paroll
        fields = "__all__"