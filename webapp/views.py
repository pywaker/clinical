
from django.utils import timezone
from django.shortcuts import render
from django.contrib import messages

from .models import Clinic, ClinicTickets, Patient
from .forms import ClinicTicketForm


# Create your views here.
def create_ticket(request):
    form = ClinicTicketForm(request.POST or None)
    clinics = Clinic.objects.values_list('id', 'name')
    form.fields['clinic'].choices = list(clinics)
    if request.method == 'POST':
        # print(form.is_valid(), '<-------')
        # print(form.errors)
        if form.is_valid():
            print(form.cleaned_data)
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
            print('------------->Hrere')
            messages.success(request, 'Ticket created successfully.')
    return render(template_name='create_ticket.html',
                  request=request, context={'form': form})
