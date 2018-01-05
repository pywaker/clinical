
from django.forms import ModelForm, BaseModelFormSet, formset_factory
from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import (Patient, Doctor, Lab, Clinic, Pharmacy, ClinicTickets,
                     LabTickets, MedicalHistory, FarmacyTickets, ClinicEmployee)


@admin.register(ClinicTickets)
class ClinicTicketsAdmin(admin.ModelAdmin):
    list_display = ('clinic', 'patient', 'assigned_to', 'assigned_on',
                    'status', 'priority', 'description')
    search_fields = ('patient__fullname',) # TODO
    list_filter = ('status', 'priority',)
    date_hierarchy = 'assigned_on'


# type('UserFormSet', (BaseModelFormSet,), {'__init__': functiona_name})
class UserFormSet(BaseModelFormSet):
    def __init__(self, instance, *args, **kwargs):
        print('------------------', instance)
        super().__init__(*args, **kwargs)


class UserForm(ModelForm):

    # def __init__(self, **kwargs):
    #     print(kwargs)

    class Meta:
        model = User
        fields = ('email', 'password')


# class ClinicEmployeeForm(ModelForm):
#     class Meta:
#         model = ClinicEmployee


class ClinicEmployeeInline(admin.StackedInline):
    model = ClinicEmployee
    # form = ClinicEmployeeForm
    formset = formset_factory(UserForm, formset=UserFormSet)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     print(args, kwargs)


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    inlines = [
        ClinicEmployeeInline
    ]


admin.site.register([Patient, Doctor, Lab, Pharmacy,
                     LabTickets, MedicalHistory,
                     FarmacyTickets])
