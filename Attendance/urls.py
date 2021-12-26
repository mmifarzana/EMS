from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', Attendance, name='Attendance'), #employee
    path('view_Attendance/', view_Attendance, name='view_Attendance'), #for admin
    path('Attendance_report/', Attendance_report, name='Attendance_report'),
    #path('admin_attendance_view/', Attendance_report, name='Attendance_report'),
    
  
  
]
