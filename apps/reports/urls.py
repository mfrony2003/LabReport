from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
    path('printBillByReport/<int:reportId>', views.printBillByReport, name="printBillByReport"),
    path('printPatientReportDetails/<int:patientDiagnosisId>/<int:reportId>', views.printPatientReportDetails, name="printPatientReportDetails"),

    
]