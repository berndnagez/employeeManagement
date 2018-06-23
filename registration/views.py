from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.template.context import RequestContext

# Create your views here.

def check_is_user_loggedin(request):
    return "AnonymousUser" != request.user.__str__()


def startpage(request):
    if check_is_user_loggedin(request):
        # _loggerinstance.log("Logged in user accessed Index-Page - (%s)" % request.user.username, "INFO")
        # return HttpResponseRedirect("/backpackpage")
        return HttpResponseRedirect("/")
    else:
        return render(request, 'startpage.html')
    #     _loggerinstance.log("Anonymous user accessed Index-Page", "INFO")
    #
    # c = _configuration.get_TrackingDictionary()
    # c.update(csrf(request))
    # return render_to_response("index.html", c)

def login_user(request):
    requestcontext = RequestContext(request)
    # username = request.POST['username']
    # password = request.POST['password']
    return render(request, 'welcomepage.html')


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
        return render_to_response("registration.html", c)

@LoginValidator
def login_user(request):
"""