
import random
from datetime import datetime, timedelta
# from django.utils
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.db.models.aggregates import Count

from webapp.models import Patient, Doctor, Clinic, Lab, Pharmacy, ClinicTickets

NAMES = ['Harry', 'Gopal', 'Madhav', 'Ron', 'Julia', 'Christine', 'Bob']
CITIES = ['Kathmandu', 'Pokhara', 'Birgunj', 'Dharan', 'Biratnagar',
            'Dhankuta', 'Illam', 'Dhangadi', 'Bhaktapur', 'Rajbiraj']
SPECIALTY = ['Surgeon', 'Pediatrics', 'Urology']
DEPARTMENT = ['Orthopedic', 'Neuro', 'General']


def create_patients():
    names = [NAMES[random.randint(0, 6)] for _ in range(0, 1000)]
    for name in names:
        name = '{}{}'.format(name.lower(), random.randint(1000, 4999))
        email = '{}_patient@example.net'.format(name.lower())
        password = '{}123'.format(name.lower())
        try:
            user = User.objects.create_user(name, email, password)
        except IntegrityError:
            continue

        obj = Patient(
            user=user,
            fullname='{} Patient'.format(name),
            address=CITIES[random.randint(0, 9)],
            phone=''.join([str(random.randint(0, 9)) for _ in range(0, 10)]),
            email=email
        )
        obj.save()


def create_doctors():
    names = [NAMES[random.randint(0, 6)] for _ in range(0, 10)]
    for name in names:
        name = '{}{}'.format(name.lower(), random.randint(11, 99))
        email = '{}_doctor@example.net'.format(name.lower())
        password = '{}123'.format(name.lower())
        try:
            user = User.objects.create_user(name, email, password)
        except IntegrityError:
            continue

        obj = Doctor(
            user=user,
            fullname='{} Doctor'.format(name),
            address=CITIES[random.randint(0, 9)],
            phone=''.join([str(random.randint(0, 9)) for _ in range(0, 10)]),
            email=email,
            specialty=SPECIALTY[random.randint(0, 2)],
            department=CITIES[random.randint(0, 2)]
        )
        obj.save()


def create_clinic():
    names = ['Bir', 'Himalayan', 'Polystar']
    for name in names:
        email = '{}_clinic@example.net'.format(name.lower())
        obj = Clinic(
            name=name,
            address=CITIES[random.randint(0, 9)],
            phone=''.join([str(random.randint(0, 9)) for _ in range(0, 10)]),
            email=email
        )
        obj.save()


def create_tickets():
    """
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    assigned_to = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    assigned_on = models.DateTimeField()
    description = models.TextField()
    status = models.CharField(max_length=16, choices=TICKET_STATUS_CHOICES)
    priority = models.PositiveSmallIntegerField(choices=TICKET_PRIORITY_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    """
    clinics = Clinic.objects.all()
    clinic_count = Clinic.objects.aggregate(count=Count('id'))['count']
    doctors = Doctor.objects.all()
    doctor_count = Doctor.objects.aggregate(count=Count('id'))['count']
    patients = Patient.objects.all()
    patient_count = Patient.objects.aggregate(count=Count('id'))['count']
    last_week = datetime.now() - timedelta(days=7)

    for i in range(0, 100000):
        assigned_date = datetime.now() + timedelta(days=random.randint(-30, 30))
        obj = ClinicTickets(
            clinic=clinics[random.randint(0, clinic_count - 1)],
            patient=patients[random.randint(0, patient_count - 1)],
            assigned_to=doctors[random.randint(0, doctor_count - 1)],
            assigned_on=assigned_date,
            description='description',
            status='open' if assigned_date > last_week else 'closed',
            priority=random.randint(1, 3)
        )
        obj.save()
