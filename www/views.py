from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def login(request):
    return HttpResponse("Login Windows")


def view_dashboard(request):
    return HttpResponse("Hello, world. You're at the Dashboard.")


def view_project_homepage(request):
    return HttpResponse("Project Homepage")


def wiki_page(request):
    return HttpResponse("Wiki Page")


def journal_page(request):
    return HttpResponse("Journal Page")


def user_settings(request):
    return HttpResponse("User settings")


def system_settings(request):
    return HttpResponse("System settings")
