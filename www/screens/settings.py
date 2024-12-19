from django.http import HttpResponse
from django.template import loader


def user_settings(request):
    return HttpResponse("User settings")


def system_settings(request):
    return HttpResponse("System settings")
