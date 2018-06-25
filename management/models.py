from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.http import HttpRequest

from django.contrib.auth.forms import PasswordResetForm

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

    # Overwirte the save-Method to add a user and send him a mail with a PW-Reset-Link
    def save(self):
        user, created = User.objects.get_or_create(username=self.Vorname, email=self.EMail)
        if created:
            user.set_password(get_random_string())
            user.save()
        super(Employee, self).save()

        request = HttpRequest()
        request.META = request.META
        request.META['SERVER_NAME'] = 'localhost'
        request.META['SERVER_PORT'] = '8000'

        reset_form = PasswordResetForm({'email': self.EMail})
        assert reset_form.is_valid()
        reset_form.save(
            request=request,
            subject_template_name='registration/password_reset_subject.txt',
            email_template_name='registration/password_reset_email.html',
        )