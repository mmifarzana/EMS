from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def Attendance(request): 
   attend = attendance.objects.all()
   context ={
    "Attend": attend
    } 
   return render(request, 'Attendance.html', context) 

def view_Attendance(request): 
   attend1 = attendance.objects.all()
   context ={
    "A_Attend": attend1
    } 
   return render(request, 'view_attendance.html', context) 

def Attendance_report(request): 
   return render(request, 'attendance_report.html')


