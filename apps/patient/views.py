import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from apps.doctors.helper import getMyDoctorByDiagnosisCategory
from apps.doctors.models import DoctorReports,Doctor
from apps.diagnosis.helper import getTotalPrice

from apps.diagnosis.models import Diagnosis, DiagnosisParameters

# Create your views here.


from .models import BloodGroup, MyPatientReport, Patient,PatientDiagnosis, PatientReportDetails

# Create your views here.
def patientdashboard(request):
    return render(request, 'patient/patientdashboard.html')

def patientAdd(request):
    return render(request, 'patient/patientadd.html')

def patientSearch(request):
  bloodGroup = BloodGroup.objects.all().values()
  patient = Patient.objects.all().values()
  diagonisis=Diagnosis.objects.all().values()
  
  context = {
    'bloodGroup': bloodGroup,
    'patient': patient,
    'diagonisis':diagonisis
  }  
  return render(request, 'patient/patientSearch.html',context)

def modal(request):
    return render(request, 'patient/modal.html')

def SavePatient(request):
     if request.method == 'POST':
        firstName = request.POST['firstName']
        age = request.POST['age']              
        lastName = request.POST['lastName']
        mobileno = request.POST['mobileno']              
        bloodGroup = request.POST['bloodGroup']
        patient = Patient(firstname=firstName,
                            lastname = lastName,    
                            age = age,
                            mobile=mobileno,
                            blood_group=BloodGroup.objects.get(id=bloodGroup),
                            created_by=request.user,
                            updated_by=request.user
                              )
        patient.save()
        
        
     return redirect("patientSearch")

def SavePatientDiagnosis(request):
        if request.method == 'POST':
        #  is_private = request.POST.get('is_private', False)
         diagnosisList = request.POST['list']
         patientId=request.POST['patientId'] 
         myPatientReport=MyPatientReport(patient_id=patientId,created_by=request.user,updated_by=request.user)
         myPatientReport.save()
         myPatientReport_id=myPatientReport.id

         doctorReports = DoctorReports( 
          doctor_id=getMyDoctorByDiagnosisCategory()['doctorId'],
          myPatientReport_id=myPatientReport_id,
          created_by=request.user,updated_by=request.user)
         doctorReports.save()

         for diagnosisId in json.loads(diagnosisList):
          patientDiagnosis = PatientDiagnosis( 
               myPatientReport_id=myPatientReport_id,
               patient_id=patientId, Diagnosis_id=diagnosisId,
               created_by=request.user,updated_by=request.user)
          patientDiagnosis.save()                    
      
              
         return  JsonResponse({'patientId':patientId, 'ReportId': myPatientReport_id})

def savePatientReportDetails(request):    
          avoidItem=['csrfmiddlewaretoken','patientDiagnosisId','reportId']          
          if request.method == 'POST':
              patientDiagnosisId=request.POST['patientDiagnosisId']
              reportId=request.POST['reportId']
              delObjPatientReportDetails=PatientReportDetails.objects.filter(patientDiagnosis_id=patientDiagnosisId)
              delObjPatientReportDetails.delete()

              for key, value in request.POST.items():
                if key not in avoidItem:                    
                    patientReportDetails = PatientReportDetails(
                        patientDiagnosis_id=patientDiagnosisId,
                        DiagnosisParameters_id=key,
                        Result=value,
                        created_by=request.user,
                        updated_by=request.user
                    )
                    patientReportDetails.save()
                    PatientDiagnosis.objects.filter(id=patientDiagnosisId, myPatientReport_id=reportId).update(isChecked=True)
          return redirect('doctordashboard')
          

def patientReportDetails(request,patientDiagnosisId,reportId):    

          patientDiagnosis = PatientDiagnosis.objects.get(id=patientDiagnosisId)
          Diagnosisid=patientDiagnosis.Diagnosis_id
          diagnosis=Diagnosis.objects.filter(id=Diagnosisid)
          patientReportDetails = DiagnosisParameters.objects.filter(diagnosisName_id=Diagnosisid )
          patientName='diagnosisName'
          diagnosisName=diagnosis.first().name
          
          context = {
            'patientReport': patientReportDetails,
            'patientName': patientName,
            'diagnosisName': diagnosisName,
            'diagnosisid':Diagnosisid,
            'patientDiagnosisId':patientDiagnosisId,
            'reportId':reportId
            
            }  
          return render(request, 'patient/patientReportDetails.html',context)

def MypatientDiagnosisList(request,patientId):               
          patientDiagnosis = PatientDiagnosis.objects.filter(patient_id=patientId).order_by('-created_at')
          patientName= Patient.objects.filter(id=patientId).first()     
          diagnosisList = {}
          total=0
          diagnosisList, total ,patientName = getTotalPrice(patientDiagnosis)
          context = {              
              'patientName': patientName, 
              'total':total
              } 
          if  patientDiagnosis:            
            context.update({'patientDiagnosis': diagnosisList})
                
            return render(request, 'patient/patientDiagnosisList.html',context)
          else:
               return render(request, 'patient/nodatafound.html',context)

def PatientReportList(request,reportId):               
          patientDiagnosis = PatientDiagnosis.objects.filter(myPatientReport_id=reportId).order_by('-created_at')
          patientName= "" 
          diagnosisList = {}
          total=0
          diagnosisList, total ,patientName = getTotalPrice(patientDiagnosis)
             
    
          context = {              
              'patientName': patientName, 
              'total':total
              } 
          
          if  patientDiagnosis:            
            context.update({'patientDiagnosis': diagnosisList})
                
            return render(request, 'patient/patientDiagnosisList.html',context)
          else:
               return render(request, 'patient/nodatafound.html',context)
def viewReportLogin(request):
     return render(request, 'patient/viewReportLogin.html')
     
def viewReport(request):    
   reportId=request.POST['reportId']          
   objPatientDiagnosis=PatientDiagnosis.objects.filter(myPatientReport_id=reportId)      
   diagnosisList, total ,patientName = getTotalPrice(objPatientDiagnosis) 
  #  doctor= DoctorReports.objects.filter(myPatientReport_id=reportId).first()
  #  print(doctor)

   context = {              
      'patientName': patientName, 
      'total':total,
      'diagnosisList':diagnosisList,
      'doctor':'doctor'
        }      
    
        
   return render(request, 'patient/patientViewReport.html',context)
     
          
          


    