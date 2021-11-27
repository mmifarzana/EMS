from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def leave(request): 
   return render(request, 'view_Leave.html') 

def admin_view_leave(request): 
   return render(request, 'admin_view.html') 

def leave_report(request): 
   return render(request, 'Leave_report.html') 


