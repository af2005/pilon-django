from django.http import HttpResponse
from django.template import loader


def view_login(request):
    return HttpResponse("Login Windows")


def view_logout(request):
    return HttpResponse("Login Windows")


def rest_login(request):
    pass


def rest_logout(request):
    pass


