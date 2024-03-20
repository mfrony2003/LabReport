"""
URL configuration for Pathology project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf import settings

from django.views.static import serve
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path,re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('apps.userauth.urls')),
     path('', include('apps.patient.urls')),
     path('', include('apps.reports.urls')),
     path('', include('apps.doctors.urls')),
     path('', include('apps.pathologist.urls')),
   
 ] 

urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})]

if not settings.DEBUG:
    handler400 = 'apps.reports.views.bad_request'
    handler403 = 'apps.reports.views.permission_denied'
    handler404 = 'apps.reports.views.page_not_found'
    handler500 = 'apps.reports.views.server_error'
