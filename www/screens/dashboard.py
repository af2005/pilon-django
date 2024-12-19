from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def view_dashboard(request):
    template = loader.get_template('www/default.html')
    context = {
        'window_title': "Dashboard",
        'page_title': "Today",
        'sidebar': True,
        'content': ""
    }
    return HttpResponse(template.render(context, request))