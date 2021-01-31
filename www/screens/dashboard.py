from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from . import default_template

SIDEBAR_ITEMS = [
    {
        'name': "Latest updates",
        'url': "#"
    }
]


def view_dashboard(request):
    tpl = default_template.get(request,
                               window_title="Dashboard",
                               title="Today",
                               sidebar=True,
                               sidebar_items=SIDEBAR_ITEMS
                               )

    return HttpResponse(tpl)
