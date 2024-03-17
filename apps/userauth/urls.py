
from django.contrib import admin
from django.urls import include, path

from apps.userauth import views

urlpatterns = [   
    
    path('', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
  
    
]
