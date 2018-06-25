from django.contrib import admin
from management.models import Employee

# Register your models here.

admin.site.register(Employee)

admin.site.site_header = "employeeManagement ";
admin.site.site_title = "employeeManagement ";