from django.contrib import admin

from apps.doctors.models import DoctorSpecialization,Doctor

# Register your models here.
admin.site.register(DoctorSpecialization)
admin.site.register(Doctor)