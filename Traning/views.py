from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def view_traning(request): 
   traningCourse = traning.objects.all()
   context ={
    "Traning": traningCourse
    }
   return render(request, 'view_traning.html', context)
   

def traning_report(request): 
   return render(request, 'traning_report.html') 

