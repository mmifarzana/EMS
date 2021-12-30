from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from .forms import *

# Create your views here.
def Add_employee(request): 
   employee_form = EmployeeForm()
   if request.method == "POST":
         employee_form = EmployeeForm(request.POST,  request.FILES)
         if employee_form.is_valid():
               employee_form.save() 
   return render(request, 'add_employee.html',{"E_form": employee_form})
     
def all_employee(request): 
   Employee = employee.objects.all()
   context ={
    "All_employee": Employee,
   }
   return render(request, 'all_employee.html', context)
      
        
def Profile(request, id):   
   try:
      profile = employee.objects.get(pk=id)
   except ObjectDoesNotExist as DoesNotExist:
      profile = None
   
   return render(request, 'profile.html', {"Pro":profile})


     
def employee_report(request): 
    return render(request, 'employee_report.html')



