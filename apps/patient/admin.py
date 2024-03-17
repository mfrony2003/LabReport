from django.contrib import admin

from .models import BloodGroup,  Patient, PatientDiagnosis

# Register your models here.
admin.site.register(BloodGroup)
admin.site.register(Patient)

admin.site.register(PatientDiagnosis)

