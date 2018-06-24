from django.db import models

# Create your models here.


class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birthDay = models.DateField()
    street = models.CharField(max_length=30)
    houseNum = models.IntegerField()
    city = models.CharField(max_length=30, default='Hamburg')
    postCode = models.IntegerField()
    overtime = models.IntegerField(default='0')
    leaveDays = models.IntegerField(default='30')

    def __str__(self):
        return self.name + ', ' + self.firstName + ' (ID: ' + str((self.id)) + ')'