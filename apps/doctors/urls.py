
from django.urls import include, path

from apps.doctors import views


urlpatterns = [       
   
   path('doctordashboard', views.doctordashboard, name='doctordashboard'),
    
    
    
    
    
]
