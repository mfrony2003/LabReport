import json
from django.http import JsonResponse
from django.shortcuts import render
from apps.diagnosis.models import Specimen
from apps.patient.models import MyPatientSpecimen, PatientDiagnosis
from apps.diagnosis.helper import getPatientDiagnosis




# Create your views here.
def pathologistdashboard(request):
   
     objPatientDiagnosis=PatientDiagnosis.objects.all()
     diagnosisList = {}
     total=0
     diagnosisList, total ,patientName = getPatientDiagnosis(objPatientDiagnosis)
     specimen = Specimen.objects.all()
     
     context = {                      
        'total':total,
        'diagnosisList':diagnosisList,
        'specimen':specimen
          }      
     
        
     return render(request, 'pathologist/pathologistdashboard.html',context)

def saveSpecimen(request):
     if request.method == 'POST':
          # Get form values
        
        saveSpecimenData = request.POST['saveSpecimenData']        
        
        data=json.loads(saveSpecimenData)        
        reportId = data['reportId']
        specimenid = data['specimenid']
        diagnosisid = data['diagnosisid']
        
        myPatientSpecimen=MyPatientSpecimen(specimen_id=specimenid,created_by=request.user,updated_by=request.user)
        myPatientSpecimen.save()
        myPatientSpecimen_id=myPatientSpecimen.id

        objPatientDiagnosis= PatientDiagnosis.objects.filter(myPatientReport_id=reportId , Diagnosis_id=diagnosisid)
        objPatientDiagnosis.update(myPatientSpecimen_id=myPatientSpecimen_id, updated_by=request.user)
            
     return  JsonResponse({'myPatientSpecimen_id':myPatientSpecimen_id})

    
     

