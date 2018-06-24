from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View

from .models import Employee
from .forms import UserForm

# Create your views here.

# def check_is_user_loggedin(request):
#     return "AnonymousUser" != request.user.__str__()
#
#
# def startpage(request):
#     if check_is_user_loggedin(request):
#         # _loggerinstance.log("Logged in user accessed Index-Page - (%s)" % request.user.username, "INFO")
#         # return HttpResponseRedirect("/backpackpage")
#         return HttpResponseRedirect("/")
#     else:
#         return render(request, 'startpage.html')
#     #     _loggerinstance.log("Anonymous user accessed Index-Page", "INFO")
#     #
#     # c = _configuration.get_TrackingDictionary()
#     # c.update(csrf(request))
#     # return render_to_response("index.html", c)


def startpage(request):
    return render(request, 'startpage.html')


# def login_user(request):
#     username = request.POST.get("inputEmail")
#     password = request.POST.get("inputPassword")
#
#     # returns User objects if credentials are correct
#     user = authenticate(username=username, password=password)
#
#     if user is not None:
#
#         if user.is_active:
#
#             allEmployee = Employee.objects.all()
#             return render(request, 'index.html', {'allEmployee' : allEmployee})
#
#         else:
#             return render(request, 'startpage.html')


# def login_user(request):
#     allEmployee = Employee.objects.all()
#     return render(request, 'index.html', {'allEmployee' : allEmployee})

# class Login_user(View):
#
#     def render(self, request):
#         allEmployee = Employee.objects.all()
#         return render(request, 'index.html', {'allEmployee' : allEmployee})


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


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            print("here we are again")

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect(login_user)

        return render(request, self.template_name, {'form': form})




"""
def view_registration_page(request):
    if check_is_user_loggedin(request):
        _loggerinstance.log("Logged in user accessed Registration-Page - (%s)" % request.user.username, "INFO")
        return HttpResponseRedirect("/backpackpage")
    else:
        _loggerinstance.log("Anonymous user accessed Registration-Page", "INFO")

        c = _configuration.get_TrackingDictionary()
        c.update(csrf(request))
        c["CurrentPopulation"] = shipAPI.get_current_population()
        c["MaximumPopulation"] = shipAPI.get_maximum_population()
        return render_to_response("management.html", c)

@LoginValidator
def login_user(request):
"""