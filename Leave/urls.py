from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', leave, name='leave_employee'), #employee
    #path('add_leave/', add_leave, name='add_leave'), 
    path('admin_view_leave/', admin_view_leave, name='admin_view_leave'),
    path('leave_report/', leave_report, name='leave_report'),
    
  
  
]
