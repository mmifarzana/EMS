from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def add_traning(request): 
   traning_form = TraningForm()
   if request.method == "POST":
         traning_form = TraningForm(request.POST,  request.FILES)
         if traning_form.is_valid():
               traning_form.save() 
   return render(request, 'add_traning.html',{"T_form": traning_form})

def view_traning(request): 
   traningCourse = traning.objects.all()
   context ={
    "Traning": traningCourse
    }
   return render(request, 'view_traning.html', context)

def appling_traning(request): 
   traningCourse1 = Applying_traning.objects.all()
   context ={
    "a_Traning": traningCourse1
    }
   return render(request, 'appling_traning.html', context)
   

def traning_report(request): 
   return render(request, 'traning_report.html') 

