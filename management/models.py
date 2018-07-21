from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator, RegexValidator
from django.http import HttpRequest
from django.contrib.auth.forms import PasswordResetForm


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=30, name='Vorname')
    name = models.CharField(max_length=30, name='Nachname')
    email = models.EmailField(max_length=254, name='EMail', validators=[EmailValidator], unique=True)
    birthDay = models.DateField(name='Geburtstag')
    street = models.CharField(max_length=30, name='Straße')
    houseNum = models.CharField(name='Hausnummer', max_length=4)
    city = models.CharField(max_length=30, default='Hamburg', name='Stadt')
    postCode = models.CharField(name='Postleitzahl', max_length=5,
                                validators=[RegexValidator(regex='([0]{1}[1-9]{1}|[1-9]{1}[0-9]{1})[0-9]{3}',
                                                           message='Bitten geben Sie eine korrekte, deutsche Postleitzahl ein.')])
    overtime = models.IntegerField(default='0', name='Überstunden')
    leaveDays = models.IntegerField(default='30', name='Urlaub')

    def __str__(self):
        return self.Nachname + ', ' + self.Vorname + ' (ID: ' + str((self.id)) + ')'

    def save(self):
        # Creating the stuff for the email
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

        super(Employee, self).save()
