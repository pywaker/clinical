from django.contrib import admin

# Register your models here.
from .models import (Patient, Doctor, Lab, Clinic, Pharmacy, ClinicTickets,
                     LabTickets, MedicalHistory, FarmacyTickets)


@admin.register(ClinicTickets)
class ClinicTicketsAdmin(admin.ModelAdmin):
    list_display = ('clinic', 'patient', 'assigned_to', 'assigned_on',
                    'status', 'priority', 'description')
    search_fields = ('patient__fullname',) # TODO
    list_filter = ('status', 'priority',)
    date_hierarchy = 'assigned_on'


admin.site.register([Patient, Doctor, Lab, Clinic, Pharmacy,
                     LabTickets, MedicalHistory,
                     FarmacyTickets])
