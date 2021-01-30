from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader, Template
from .snippets import forms
from ..models import Project


def view_create(request):
    html = '<form action="rest/project" method="POST" class="my-4">'

    html += forms.Textfield("project_key", "Project Key").render()
    html += forms.Textfield("project_fullname", "Name").render()
    html += forms.SubmitButton("Create").render()

    html += "</form>"

    template = loader.get_template('www/default.html')
    context = {
        'window_title': "Create project",
        'page_title': "Create new project",
        'sidebar': False,
        'page_subtitle': "Every projects needs a key (consisting out of a few letters or numbers) and a name.",
        'content': html,
    }
    return HttpResponse(template.render(context, request))


def view_directory(request):
    template = loader.get_template('www/default.html')
    context = {
        'window_title': "Project directory",
        'page_title': "Project Directory",
        'page_subtitle': "All Projects visible to you",
        'sidebar': False,

    }
    return HttpResponse(template.render(context, request))


def view_homepage(request):
    pass
