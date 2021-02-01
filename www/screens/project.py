from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader, Template
from .snippets import forms
from ..models import Project
from . import templates


@login_required
def view_create(request):
    template = loader.get_template('www/project/create.html')
    context = {
        'window_title': "Create project",
        'page_title': "Create new project",
        'page_subtitle': "Every projects needs a key (consisting out of a few letters or numbers) and a name.",
        'content': ""
    }

    return HttpResponse(template.render(context, request))


@login_required
def view_directory(request):
    tpl = templates.simple(request,
                           window_title="Project directory",
                           title="Project Directory",
                           subtitle="All Projects visible to you",
                           )

    return HttpResponse(tpl)


@login_required
def view_homepage(request):
    pass
