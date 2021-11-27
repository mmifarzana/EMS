from django import forms
from .models import *
  
class ParollForm(forms.ModelForm):
  
    class Meta:
        model = Paroll
        fields = "__all__"