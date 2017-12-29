from django.db import models


TICKET_STATUS_CHOICES = (
    ('open', 'Open'),
    ('closed', 'Closed')
)

TICKET_PRIORITY_CHOICES = (
    (3, 'High'),
    (2, 'Medium'),
    (1, 'Low')
)

# Create your models here.
class Patient(models.Model):
    fullname = models.CharField(max_length=128)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=128)

    def __repr__(self):
        return self.fullname

    __str__ = __repr__


class Doctor(models.Model):
    fullname = models.CharField(max_length=128)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=128)
    specialty = models.CharField(max_length=128)
    department = models.CharField(max_length=128)

    def __repr__(self):
        return self.fullname

    __str__ = __repr__


class Clinic(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=128)

    def __repr__(self):
        return self.name

    __str__ = __repr__


class Lab(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=128)

    def __repr__(self):
        return self.name

    __str__ = __repr__


class Pharmacy(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=128)

    def __repr__(self):
        return self.name

    __str__ = __repr__


class ClinicTickets(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    assigned_to = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    assigned_on = models.DateTimeField()
    description = models.TextField()
    status = models.CharField(max_length=16, choices=TICKET_STATUS_CHOICES)
    priority = models.PositiveSmallIntegerField(choices=TICKET_PRIORITY_CHOICES)

    def __repr__(self):
        return self.status

    __str__ = __repr__