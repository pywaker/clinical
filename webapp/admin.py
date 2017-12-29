from django.contrib import admin

# Register your models here.
from .models import Patient, Doctor, Lab, Clinic, Pharmacy, ClinicTickets

admin.site.register([Patient, Doctor, Lab, Clinic, Pharmacy, ClinicTickets])