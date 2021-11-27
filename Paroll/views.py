from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def view_salary(request): 
   return render(request, 'view_salary.html') 

def salary_report(request): 
   return render(request, 'salary_report.html') 

