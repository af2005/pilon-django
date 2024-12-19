from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader, Template
from .snippets import forms
from ..models import Project
from . import templates


def sidebar_items(key):
    return [
        {
            'name': "Homepage",
            'url': f"/project/contents/{key}",
        },
        {
            'name': "Tasks",
            'url': f"/project/contents/{key}/tasks",
        },
        {
            'name': "Calendar",
            'url': f"/project/contents/{key}/calendar",
        },
        {
            'name': "Wiki",
            'url': f"/project/contents/{key}/wiki",
        },
        {
            'name': "Journal",
            'url': f"/project/contents/{key}/journal",
        }
    ]


@login_required
def view_project_create(request):
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
    tpl = templates.project_directory(request, projects=Project.objects.all())
    return HttpResponse(tpl)


@login_required
def view_homepage(request, key):
    tpl = templates.project_homepage(request, key, sidebar_items=sidebar_items(key))
    return HttpResponse(tpl)
