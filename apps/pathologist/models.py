from django.db import models
from apps.userauth.models import GenericlInfo

from apps.patient.models import GenericUserInfo

# Create your models here.


class PathologistSpecialization(GenericlInfo):
    name = models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.name


    
class Pathologist(GenericUserInfo):
    specialization = models.ForeignKey(PathologistSpecialization, on_delete=models.CASCADE, null=True, blank=True)

