
from django.forms import ModelForm, BaseModelFormSet, formset_factory, modelformset_factory
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth.admin import UserAdmin
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
# class UserFormSet(BaseModelFormSet):
#     def __init__(self, instance, *args, **kwargs):
#         print('------------------', instance)
#         super().__init__(*args, **kwargs)


# class UserForm(ModelForm):

#     # def __init__(self, **kwargs):
#     #     print(kwargs)

#     class Meta:
#         model = User
#         fields = ('email', 'password')


# class ClinicEmployeeForm(ModelForm):
#     class Meta:
#         model = ClinicEmployee
#         fields = ('user', 'role', 'department', 'clinic')


# class UserAdminInline(admin.StackedInline):
#     model = User
#     formset = modelformset_factory(User, fields=('username', 'password',))


@admin.register(ClinicEmployee)
class ClinicEmployeeAdmin(admin.ModelAdmin):
    # form = ClinicEmployeeForm
    # inlines = [
    #     UserAdminInline
    # ]
    
    def save_model(self, request, obj, form, change):
        # print(request.user.clinicemployee)
        # try:
        #     user_role = request.user.clinicemployee.role == 'admin'
        # except ClinicEmployee.DoesNotExist as exp:
        #     raise PermissionDenied("Not allowed to add/update user")
        # else:
        #     print(user_role)
        #     # only then this user is able to add new user
        #     # also set current clinic as this user's default
        super().save_model(request, obj, form, change)

    def get_fieldsets(self, request, obj=None):
        try:
            user_role = request.user.clinicemployee.role == 'admin'
        except ClinicEmployee.DoesNotExist as exp:
            # fieldsets = self.get_fieldsets(request, obj)
            # print(fieldsets)
            fieldsets = (
                # ('User Panel', {'fields': ('username', 'password1', 'password2')}),
                ('Info Panel', {'fields': ('role', 'department')}),
            )
        else:
            fieldsets = (
                ('User Panel', {'fields': ('username', 'password1', 'password2')}),
            )
        return fieldsets


# class ClinicEmployeeInline(admin.StackedInline):
#     model = ClinicEmployee
#     # form = ClinicEmployeeForm
#     formset = formset_factory(UserForm, formset=UserFormSet)

#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     print(args, kwargs)


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    # inlines = [
    #     ClinicEmployeeInline
    # ]
    pass


admin.site.register([Patient, Doctor, Lab, Pharmacy,
                     LabTickets, MedicalHistory,
                     FarmacyTickets])
