from apps.diagnosis.models import DiagnosisCategory
from apps.doctors.models import Doctor
import random

def getMyDoctorByDiagnosisCategory():    
  
   doctors=Doctor.objects.all()
   doctor = random.sample( list(doctors), 1)
   doctorList=[]
   for d in doctor:            
    doctorList.append({'id':d.id, 'Name':d.firstname + d.lastname })
           

   foundDoctor={
       "doctorId":doctorList[0]['id'],
       "doctorName":f"{doctorList[0]['Name']}"
   }
   
   
   return (foundDoctor )