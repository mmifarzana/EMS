from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def Add_salary(request): 
   Paroll_Form = ParollForm()
   if request.method == "POST":
         Paroll_Form = ParollForm(request.POST,  request.FILES)
         if Paroll_Form.is_valid():
               Paroll_Form.save() 
   return render(request, 'add_salary.html',{"P_form": Paroll_Form})
 
def view_salary(request): 
   salaryCourse = paroll.objects.all()
   context ={
    "Paroll":  salaryCourse
    }
   return render(request, 'view_salary.html', context)


def salary_report(request): 
   return render(request, 'salary_report.html') 

