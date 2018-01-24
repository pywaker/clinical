
import os
import csv
import logging
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Prefetch, Q
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.conf import settings

from .models import Clinic, ClinicTickets, Patient, Doctor
from .forms import ClinicTicketForm
from .serializers import PatientSerializer


logger = logging.getLogger('django')


def list_patients_by(username, phone):
    # return Patient.objects.filter(fullname__startswith=fullname).all()
    # q = Q(status='open')
    return (Q(user__username__icontains=username) & Q(phone__contains=phone))


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


def search_patients(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        patient_query = list_patients_by(fullname, phone)
        print(patient_query)
        patients_all = Patient.objects.filter(patient_query).all()
        paginator = Paginator(patients_all, 10)
        page = request.GET.get('page', 1)
        patients = paginator.get_page(page)
        return render(template_name='list_patients.html',
                      request=request, context={'patients': patients})
    else:
        return redirect(to='list_patients')


def download_patients(request):
    patients_all = Patient.objects.prefetch_related(Prefetch('user')).all()
    filename = os.path.join(settings.TEMP_MEDIA_PATH, 'patients.csv')
    with open(filename, 'w') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=['id', 'username', 'fullname'])
        csvwriter.writeheader()
        for patient in patients_all:
            csvwriter.writerow({
                'id': patient.id,
                'username': patient.user.username,
                'fullname': patient.fullname
            })

    with open(filename, 'r') as csvfile:
        response = HttpResponse(csvfile.read(), content_type="text/csv")
        response['Content-Disposition'] = 'inline; filename=patients.csv'
        return response


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
