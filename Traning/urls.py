from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', view_traning, name='view_traning'), #employee
    path('add_traning/', add_traning, name='add_traning'), 
    #path('admin_view_leave/', admin_view_leave, name='admin_view_leave'),
    path('traning_report/', traning_report, name='traning_report'),
    path('appling_traning/', appling_traning, name='appling_traning'),
    
  
  
]
