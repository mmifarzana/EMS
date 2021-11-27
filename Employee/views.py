from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def all_employee(request): 
   
   return render(request, 'all_employee.html')

def Profile(request): 
   return render(request, 'profile.html')

def employee_report(request): 
   return render(request, 'employee_report.html')


