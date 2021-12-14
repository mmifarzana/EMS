from django import forms
from .models import *
  
class TraningForm(forms.ModelForm):
  
    class Meta:
        model = traning
        fields = "__all__"