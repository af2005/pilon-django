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
    tpl = templates.default(request,
                        window_title="Dashboard",
                        title="Today",
                        sidebar=True,
                        sidebar_items=SIDEBAR_ITEMS
                        )

    return HttpResponse(tpl)
