from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

def leave(request): 
   qury_set = leave.objects.all() 
   context = {
    "Leave": qury_set
    }
   return render(request, 'view_Leave.html', context) 

def admin_view_leave(request): 
   return render(request, 'admin_view.html') 

def leave_report(request): 
   return render(request, 'Leave_report.html') 


