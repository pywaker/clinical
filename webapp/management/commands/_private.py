
import random
from django.db.utils import IntegrityError
from django.contrib.auth.models import User

from webapp.models import Patient, Doctor, Clinic, Lab, Pharmacy

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
    names = [NAMES[random.randint(0, 6)] for _ in range(0, 1000)]
    for name in names:
        name = '{}{}'.format(name.lower(), random.randint(5000, 9999))
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
