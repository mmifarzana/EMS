from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def add_leave(request): 
   leave_Form = LeaveForm()
   if request.method == "POST":
         leave_Form = LeaveForm(request.POST,  request.FILES)
         if leave_Form.is_valid():
               leave_Form.save() 
   return render(request, 'Add_Leave.html',{"L_form": leave_Form})

def leave (request): 
   leave = Leave.objects.all()
   context ={
    "leave_e": leave,
   }
   return render(request, 'view_Leave.html', context)

def admin_view_leave (request): 
   leave1 = Leave.objects.all()
   context ={
    "a_leave": leave1,
   }
   return render(request, 'admin_view.html', context)


def leave_report(request): 
   return render(request, 'Leave_report.html') 


