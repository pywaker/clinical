
import logging
from django.utils import timezone
from django.shortcuts import render
from django.contrib import messages
from django.db.models import Prefetch
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import Clinic, ClinicTickets, Patient, Doctor
from .forms import ClinicTicketForm
from .serializers import PatientSerializer


logger = logging.getLogger('django')



# Create your views here.
def create_ticket(request):
    # print(logger)
    form = ClinicTicketForm(request.POST or None)
    clinics = Clinic.objects.values_list('id', 'name')
    form.fields['clinic'].choices = list(clinics)
    if request.method == 'POST':
        # print(form.is_valid(), '<-------')
        # print(form.errors)
        if form.is_valid():
            # print(form.cleaned_data)
            clinic = Clinic.objects.get(pk=form.cleaned_data['clinic'])
            ticket = ClinicTickets(
                clinic=clinic,
                patient=Patient.objects.get(pk=1),
                assigned_on=timezone.now(),
                description=form.cleaned_data['description'],
                status='open',
                priority=2
            )
            ticket.save()
            # print('------------->Hrere')
            logger.info("successfully saved.")
            messages.success(request, 'Ticket created successfully.')
    return render(template_name='create_ticket.html',
                  request=request, context={'form': form})


def list_doctors(request):
    doctors = Doctor.objects.prefetch_related(Prefetch('user')).all()
    return render(template_name='list_doctors.html',
                  request=request, context={'doctors': doctors})


def list_patients(request):
    patients_all = Patient.objects.prefetch_related(Prefetch('user')).all()

    # limit = int(request.GET.get('limit', 10))
    # offset = (page - 1) * limit
    # patients = patients_all[offset:(page * limit)]

    paginator = Paginator(patients_all, 10)
    page = request.GET.get('page', 1)
    patients = paginator.get_page(page)
    return render(template_name='list_patients.html',
                  request=request, context={'patients': patients})


@csrf_exempt
def patient_list(request):
    patients_all = Patient.objects.all()
    serializer = PatientSerializer(patients_all, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_patient(request, patient_id):
    patients_all = Patient.objects.get(pk=patient_id)
    serializer = PatientSerializer(patients_all)
    return JsonResponse(serializer.data)
