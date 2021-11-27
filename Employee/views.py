from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
 
def all_employee(request): 
   Employee = emplyee.objects.all()
   context ={
    "All_employee": Employee,
   }
   return render(request, 'all_employee.html', context)

def Profile(request): 
   return render(request, 'profile.html')

def employee_report(request): 
   return render(request, 'employee_report.html')


