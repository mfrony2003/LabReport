from django.db import models
from apps.diagnosis.models import DiagnosisCategory
from apps.userauth.models import GenericlInfo, User

from apps.patient.models import GenericUserInfo, MyPatientReport



# Create your models here.

class DoctorSpecialization(GenericlInfo):
    name = models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.name


    
class Doctor(GenericUserInfo):    
    specialization = models.ForeignKey(DoctorSpecialization, on_delete=models.CASCADE, null=True, blank=True)
    diagnosisCategory=models.ForeignKey(DiagnosisCategory, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return "{0} {1}--{2}-------{3}".format(self.firstname ,  self.lastname , self.specialization.name, self.diagnosisCategory.name)

class DoctorReports(GenericlInfo):    
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  myPatientReport = models.ForeignKey(MyPatientReport, on_delete=models.CASCADE)  

  def __str__(self):
        return self.doctor
      