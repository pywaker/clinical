from django.contrib import admin

# Register your models here.
from .models import (Patient, Doctor, Lab, Clinic, Pharmacy, ClinicTickets,
                     LabTickets, MedicalHistory, FarmacyTickets)


admin.site.register([Patient, Doctor, Lab, Clinic, Pharmacy,
                     ClinicTickets, LabTickets, MedicalHistory,
                     FarmacyTickets])
