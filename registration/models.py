from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    birthDay = models.DateField()
    street = models.CharField(max_length=30)
    houseNum = models.IntegerField()
    postCode = models.IntegerField()
    overtime = models.IntegerField()
    leaveDays = models.IntegerField()