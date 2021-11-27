from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def view_traning(request): 
   return render(request, 'view_traning.html') 

def traning_report(request): 
   return render(request, 'traning_report.html') 

