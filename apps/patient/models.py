from django.db import models
from apps.diagnosis.models import Diagnosis,DiagnosisParameters, Specimen

from apps.userauth.models import GenericlInfo, User

# Create your models here.
class GenericUserInfo(GenericlInfo):
    # Personal Information
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)    
    age = models.IntegerField()
    address = models.CharField(max_length=200)    
    picture= models.ImageField(upload_to='profile_pics',blank=True)
    # Contact Information
    address= models.CharField(max_length=200)
    city= models.CharField(max_length=200)
    state= models.CharField(max_length=200)
    zip= models.CharField(max_length=200)
    mobile= models.CharField(max_length=200)   
    class Meta:
        abstract = True
        ordering = ['-created_at']
    def __str__(self):
        return self.firstname

class BloodGroup(GenericlInfo):
    # List of Blood Groups
    name = models.CharField(max_length=20)    
    def __str__(self):
        return f"{self.name}"    
    
class PatientManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_active=True)
    
class Patient(GenericUserInfo):
    # Medical Information
    
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, null=True, blank=True)
    allergies = models.TextField()
    diseases = models.TextField()
    objects=PatientManager()
    admin_objects = models.Manager()

    def __str__(self):
        return f"PatientId-{self.id} Name: {self.firstname} {self.lastname}"
    
    def getatientId(self):
        return "PT"+ 100000 + {self.id}
    


    

class MyPatientReport(GenericlInfo):
    # Medical Information
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)    
    
    def __str__(self):
        return  f"{self.patient.firstname} {self.patient.lastname}"    
    

class MyPatientSpecimen(GenericlInfo):
    
    specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
       return f"{self.specimen}"


class PatientDiagnosis(GenericlInfo):
    # Medical Information
    myPatientReport=models.ForeignKey(MyPatientReport, on_delete=models.CASCADE,null=True, blank=True)     
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)    
    myPatientSpecimen=models.ForeignKey(MyPatientSpecimen, on_delete=models.CASCADE,null=True, blank=True)
    Diagnosis=models.ForeignKey(Diagnosis, on_delete=models.CASCADE,blank=True)   
    isChecked = models.BooleanField(default=False)
    def __str__(self):
        return  f"{self.Diagnosis.name}"
    
    
    def getReportList(self):
        return   '{0} - {1}'.format(self.Diagnosis.name,self.Diagnosis.price)
    
        
class PatientReportDetails(GenericlInfo):
    # Medical Information
    
    patientDiagnosis = models.ForeignKey(PatientDiagnosis, on_delete=models.CASCADE, null=True, blank=True)        
    DiagnosisParameters=models.ForeignKey(DiagnosisParameters, on_delete=models.CASCADE,null=True,blank=True)
    Result= models.TextField(null=True,blank=True)
    def __str__(self):
        return  f"{self.patientDiagnosis.Diagnosis.name} {self.DiagnosisParameters.investigationName} - {self.patientDiagnosis.patient.firstname} {self.patientDiagnosis.patient.lastname}"