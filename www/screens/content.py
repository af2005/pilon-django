from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def view_dashboard(request):
    template = loader.get_template('www/default-without-sidebar.html')
    context = {
        'window_title': "Dashboard",
        'page_title': "Today",

    }
    return HttpResponse(template.render(context, request))


def view_project_homepage(request):
    return HttpResponse("Project Homepage")


def wiki_page(request):
    return HttpResponse("Wiki Page")


def journal_page(request):
    return HttpResponse("Journal Page")