from django.db import models
from apps.patient.models import MyPatientReport
from apps.userauth.models import GenericlInfo

# Create your models here.
class Bill(GenericlInfo):    
    myPatientReport=models.ForeignKey(MyPatientReport, on_delete=models.CASCADE,null=True, blank=True)  
    totalAmount=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status=models.CharField(max_length=10, choices=(('Paid','Paid'),('Pending','Pending')), default='Pending')
  
    def __str__(self):
     return self.myPatientReport.Id + " " +self.myPatientReport.patient.firstname + " " + self.myPatientReport.patient.lastname + " - " + str(self.totalAmount) 