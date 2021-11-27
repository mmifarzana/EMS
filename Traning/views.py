from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def view_traning(request): 
   Tranin = traning.objects.all()
   context ={
    "Traning": traning,
   }
   return render(request, 'view_traning.html', context)
   
   return render(request, 'view_traning.html') 

def traning_report(request): 
   return render(request, 'traning_report.html') 

