from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader, Template
from .snippets import forms
from ..models import Project
from . import templates


@login_required
def main(request):
    tpl = templates.simple(request,
                           window_title="User settings",
                           title="User settings",
                           navbar_centertext="User settings"
                           )

    return HttpResponse(tpl)