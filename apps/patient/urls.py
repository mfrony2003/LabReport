from django.contrib import admin
from django.urls import include, path
from apps.patient import views

urlpatterns = [       
   
    path('staffdashboard', views.patientSearch, name='staffdashboard'),
    path('patientdashboard', views.patientSearch, name='patientdashboard'),
    
    path('patientAdd', views.patientAdd, name='patientAdd'),
    path('patientSearch', views.patientSearch, name='patientSearch'),
    path('modal', views.modal, name='modal'),
    path('SavePatient', views.SavePatient, name='SavePatient'),
    path('patientReportDetails/<int:patientDiagnosisId>/<int:reportId>', views.patientReportDetails, name='patientReportDetails'),
    path('patientDiagnosisList/<int:patientId>', views.MypatientDiagnosisList, name='patientDiagnosisList'),
    path('patientReportList/<int:reportId>', views.PatientReportList, name='patientReportList'),
    path('savePatientDiagnosis/', views.SavePatientDiagnosis, name='savePatientDiagnosis'),
    path('savePatientReportDetails/', views.savePatientReportDetails, name='savePatientReportDetails'),
    path('viewReport', views.viewReport, name='viewReport'),
    path('viewReportLogin', views.viewReportLogin, name='viewReportLogin'),
    
    
    
    
    
]
