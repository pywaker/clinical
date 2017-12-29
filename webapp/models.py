from django.db import models

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