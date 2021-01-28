from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader, Template

from ..models import Project


def view_create(request):
    html = '<form action="rest/project" method="POST">'

    html += loader.get_template('www/snippets/forms/long-text-field.html').render({
        "name": "project_key",
        "description": "Project Key"
    }, request)

    html += loader.get_template('www/snippets/forms/long-text-field.html').render({
        "name": "project_fullname",
        "description": "Name"
    }, request)

    html += loader.get_template('www/snippets/forms/submit-button.html').render({
        "text":"Create"
    }, request)

    html += "</form>"

    template = loader.get_template('www/default-without-sidebar.html')
    context = {
        'window_title': "Create project",
        'page_title': "Create new project",
        'page_subtitle': "Every projects needs a key (consisting out of a few letters or numbers) and a name.",
        'content': html,
    }
    return HttpResponse(template.render(context, request))


def view_directory(request):
    template = loader.get_template('www/default-without-sidebar.html')
    context = {
        'window_title': "Project directory",
        'page_title': "Project Directory",
        'page_subtitle': "All Projects visible to you",

    }
    return HttpResponse(template.render(context, request))


def view_homepage(request):
    pass
