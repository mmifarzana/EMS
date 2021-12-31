from django import forms
from .models import Circular, Applyparticipent

class CircularForm(forms.ModelForm):
     
     last_date_apply = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date', 'class': "form-control"}))
     date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date', 'class': "form-control"})) 
         
     class Meta:
          model = Circular
          exclude=['action']
         
class ApplyparticipentForm(forms.ModelForm):
     
     #cv = forms.FileField(widget=forms.NumberInput(attrs={'type': 'file', 'class': "form-control"}))
         
     class Meta:
          model = Applyparticipent
          exclude=['action']