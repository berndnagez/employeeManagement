from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import Employee


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # employeeData =  Employee.objects.filter(user=request.user)
                # employeeData = Employee.objects.filter(EMail=request.user.email)
                allEmployee = Employee.objects.all()
                return render(request, 'index.html', {'allEmployee': allEmployee})
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')