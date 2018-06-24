from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    firstName = models.CharField(max_length=30, name='Vorname')
    name = models.CharField(max_length=30, name='Nachname')
    email = models.EmailField(max_length=254, name='EMail')
    birthDay = models.DateField(name='Geburtstag')
    street = models.CharField(max_length=30, name='Straße')
    houseNum = models.IntegerField(name='Hausnummer')
    city = models.CharField(max_length=30, default='Hamburg', name='Stadt')
    postCode = models.IntegerField(name='Postleitzahl')
    overtime = models.IntegerField(default='0', name='Überstunden')
    leaveDays = models.IntegerField(default='30', name='Urlaub')

    def __str__(self):
        return self.Nachname + ', ' + self.Vorname + ' (ID: ' + str((self.id)) + ')'