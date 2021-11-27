from django import forms
from .models import *
  
class TraningForm(forms.ModelForm):
  
    class Meta:
        model = Traning
        fields = "__all__"