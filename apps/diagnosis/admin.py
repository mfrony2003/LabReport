from django.contrib import admin

from .models import DiagnosisCategory,Diagnosis,DiagnosisParameters,Specimen

# Register your models here.
admin.site.register(DiagnosisCategory)
admin.site.register(Diagnosis)

admin.site.register(DiagnosisParameters)
admin.site.register(Specimen)