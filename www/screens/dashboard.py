from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from . import templates

SIDEBAR_ITEMS = [
    {
        'name': "Latest updates",
        'url': "#"
    }
]


def view_dashboard(request):
    tpl = templates.dashboard(request,
                              window_title="Dashboard",
                              title="Today",
                              sidebar_items=SIDEBAR_ITEMS
                              )

    return HttpResponse(tpl)
