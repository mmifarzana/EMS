from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', view_salary, name='view_salary'), #employee
    #path('add_leave/', add_leave, name='add_leave'), 
    #path('admin_view_leave/', admin_view_leave, name='admin_view_leave'),
    path('salary_report/', salary_report, name='salary_report'),
    
  
  
]
