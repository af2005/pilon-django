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
    template = loader.get_template('www/login.html')
    context = {
        'window_title': "Login",
        'warning': "",
        'logout': True
    }
    return HttpResponse(template.render(context, request))
