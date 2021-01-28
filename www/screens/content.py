from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def view_dashboard(request):
    return HttpResponse("Hello, world. You're at the Dashboard.")


def view_project_homepage(request):
    return HttpResponse("Project Homepage")


def wiki_page(request):
    return HttpResponse("Wiki Page")


def journal_page(request):
    return HttpResponse("Journal Page")