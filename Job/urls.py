from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', Circular, name='Circular'), 
    path('add_circular/', add_circular, name='add_circular'), 
    path('Applyparticipent/', Applyparticipent, name='Applyparticipent'),
    path('Add_Applyparticipent/', Add_Applyparticipent, name='Add_Applyparticipent'),
    #path('appling_traning/', appling_traning, name='appling_traning'),
    
  
  
]
