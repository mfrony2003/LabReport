
from django.urls import include, path

from apps.pathologist import views


urlpatterns = [       
   
    path('pathologistdashboard', views.pathologistdashboard, name='pathologistdashboard'),
    path('saveSpecimen', views.saveSpecimen, name='saveSpecimen'),
    
    
    
    
    
]
