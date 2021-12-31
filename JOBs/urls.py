from django.urls import path, include
from JOBs.views import *

urlpatterns = [
    path('', view_circular, name="view_circular"),
    path('add_requrement/', addreq, name="requrement"),
    path('add_particepent/', addparticipent, name="participent"),
    path('circular_report/', index, name="Jobs"),
    path('participent_report/', participent_report, name="participent_reports"),
    path('<int:id>/', edit_job, name="edit_jobs"),
    path('<int:id>/delete', delete_job, name="delete_jobs"),
    
  
]
