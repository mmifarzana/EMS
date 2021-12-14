from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', all_employee, name='all_employee'),
    path('Profile/', Profile, name='profile'),
    path('employee_report', employee_report, name='employee_report'),
    path('Add_employee/', Add_employee, name='Add_employee'),
    
  
  
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)