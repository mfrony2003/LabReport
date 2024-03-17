import barcode 
from django.shortcuts import render

import base64
from apps.doctors.models import DoctorReports
from apps.reports.helper import createBarCodes, image_as_base64
from apps.diagnosis.helper import getTotalPrice

# Create your views here.
from apps.patient.models import PatientDiagnosis, PatientReportDetails
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.db.models import Sum

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


data = {
    "company": "Dennnis Ivanov Company",
    "address": "123 Street name",
    "city": "Vancouver",
    "state": "WA",
    "zipcode": "98663",


    "phone": "555-555-2345",
    "email": "youremail@dennisivy.com",
    "website": "dennisivy.com",
    }

#Opens up page as PDF
class ViewPDF(View):
    def get(self, request, *args, **kwargs):

        pdf = render_to_pdf('reports/patientReportDetails.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        
        pdf = render_to_pdf('reports/patientReportDetails.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("12341231")
        content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    
def index(request):
    context = {}
    return render(request, 'app/index.html', context)

def printBillByReport(request,reportId):    
   patientDiagnosis = PatientDiagnosis.objects.filter(myPatientReport_id=reportId)
   diagnosisList = {}   
   total=0
   diagnosisList, total ,patientName = getTotalPrice(patientDiagnosis)      
   encoded_string=base64.b64encode(createBarCodes(reportId))
   barcode= "data:image/jpeg;base64," + encoded_string.decode('utf-8')

   context = {              
              'patientDiagnosis': diagnosisList,   
              'total': total,              
              'barcode':barcode,
              'patientName':patientName
              
              }
   
   
   return PrintBillPDF(context)

def printPatientReportDetails(request, patientDiagnosisId, reportId):
   patientReportDetails = PatientReportDetails.objects.filter(patientDiagnosis_id=patientDiagnosisId)   
   firstObjpatientReportDetails=patientReportDetails.first().patientDiagnosis
   patientName=firstObjpatientReportDetails.patient
   diagnosisName=firstObjpatientReportDetails.Diagnosis.name
   doctorReports = DoctorReports.objects.get(myPatientReport_id=reportId)
   encoded_string=base64.b64encode(createBarCodes(reportId))
   barcode= "data:image/jpeg;base64," + encoded_string.decode('utf-8')
 

   context = {
              'patientReportDetails': patientReportDetails,              
              'reportId':reportId,
              'doctorName':doctorReports.doctor,
              'barcode':barcode,
              'patientName':patientName,
              'diagnosisName':diagnosisName


              }
  
   return PrintPatientReportDetails(context)

def PrintPatientReportDetails(data):
                
        
        try :
            pdf = render_to_pdf('reports/patientReportDetails.html', data)        
            
            response = HttpResponse(pdf, content_type='application/pdf')
            
            filename = "reort_%s.pdf" %('36584')
            
            content = "attachment; filename='%s'" %(filename)
            
            response['Content-Disposition'] = content
            return response
        except Exception as e:
          
            raise e

def PrintBillPDF(data):
                
        
        try :
            pdf = render_to_pdf('reports/patientReportBill.html', data)        
            
            response = HttpResponse(pdf, content_type='application/pdf')
            
            filename = "Invoice_%s.pdf" %("12341231")
            
            content = "attachment; filename='%s'" %(filename)
            
            response['Content-Disposition'] = content
            return response
        except Exception as e:
          
            raise e



def bad_request(request, exception, template_name="400.html"):
    context = {}
    return render(request, 'error/400.html', context, status=400)


def permission_denied(request, exception, template_name="403.html"):
    context = {}
    return render(request, 'error/403.html', context, status=403)

def page_not_found(request, exception, template_name="404.html"):
    context = {}
    return render(request, 'error/404.html', context, status=404)


def server_error(request):
    context = {}
    return render(request, 'error/500.html', context, status=500)