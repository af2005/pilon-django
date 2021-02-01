from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


@login_required
def view_project_homepage(request):
    return HttpResponse("Project Homepage")


@login_required
def wiki_page(request):
    return HttpResponse("Wiki Page")


@login_required
def journal_page(request):
    return HttpResponse("Journal Page")
