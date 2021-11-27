from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def Attendance(request): 
   return render(request, 'Attendance.html') 

def view_Attendance(request): 
   return render(request, 'view_attendance.html') 

def Attendance_report(request): 
   return render(request, 'attendance_report.html')


