from django.db import models

from apps.userauth.models import GenericlInfo

# Create your models here.

class DiagnosisCategory(GenericlInfo):
    name = models.CharField(max_length=255, blank=True, default='')
    description = models.CharField(max_length=255, blank=True, default='')
    
    def __str__(self):
     return self.name

class Specimen(GenericlInfo):
    name = models.CharField(max_length=255, blank=True, default='')
    description = models.CharField(max_length=255, blank=True, default='')
    
    def __str__(self):
     return self.name
    
class Diagnosis(GenericlInfo):
    name = models.CharField(max_length=255, blank=True, default='')    
    description = models.CharField(max_length=255, blank=True, default='')
    specimen=models.ForeignKey(Specimen, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(DiagnosisCategory, on_delete=models.CASCADE, null=True, blank=True)
    price= models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
     return '{0} - {1} - {2}'.format(self.category, self.name,self.price)
    

    
class DiagnosisParameters(GenericlInfo): 
    diagnosisName=models.ForeignKey(Diagnosis, on_delete=models.CASCADE, null=True, blank=True)
    investigationName = models.CharField(max_length=255, blank=True, default='')    
    Unit=models.CharField(max_length=255, blank=True, default='')    
    Reverence_Range=models.CharField(max_length=255, blank=True, default='')    
  
    def __str__(self):
     return '{0} -{1} '.format(self.diagnosisName, self.investigationName )