from django.http import HttpResponse
from django.template import loader


def view_login(request):
    template = loader.get_template('www/login.html')
    context = {
        'window_title': "Login",
        'warning': ""
    }
    return HttpResponse(template.render(context, request))


def view_logout(request):
    return HttpResponse("Login Windows")


def rest_login(request):
    pass


def rest_logout(request):
    pass


