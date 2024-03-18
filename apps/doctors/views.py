from django.shortcuts import render
from apps.patient.models import PatientDiagnosis
from apps.diagnosis.helper import getPatientDiagnosis
from apps.doctors.models import  Doctor, DoctorReports



# Create your views here.
def doctordashboard(request):
    diagnosisList = {}
    alldiagnosis={}
    patientName=''
    total=0  
    doctor= Doctor.objects.get(user_id=request.user.id)    
    doctorReports = DoctorReports.objects.filter(doctor_id=doctor.id)
    if not doctorReports :  
      return render(request, 'doctors/nodatafound.html')
    else:
      for doctorReport in doctorReports:
       objPatientDiagnosis=PatientDiagnosis.objects.filter(myPatientReport_id=doctorReport.myPatientReport_id)
      
       diagnosisList, total ,patientName = getPatientDiagnosis(objPatientDiagnosis)      
         
       alldiagnosis.update(diagnosisList)
      
        
     
    context = {              
        'patientName': patientName, 
        'total':total,
        'diagnosisList':alldiagnosis,
        'doctor':doctor
          }      
     
        
    return render(request, 'doctors/doctordashboard.html',context)


