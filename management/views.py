from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import Employee


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                allEmployee = Employee.objects.all()
                return render(request, 'index.html', {'allEmployee': allEmployee})
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return render(request, 'login.html')