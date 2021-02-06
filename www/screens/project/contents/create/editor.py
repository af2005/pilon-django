from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader, Template
from www.screens.snippets import forms
from www.models import Project
from www.screens import templates


def view_default_editor(request, key):
    tpl = templates.default_editor(request, title="Create Content", key=key, subtitle="In project")
    return HttpResponse(tpl)


def view_markdown_editor(request, key):
    tpl = templates.markdown_editor(request, title="Create Content", key=key, subtitle="In project")
    return HttpResponse(tpl)


def view_file_upload(request, key):
    tpl = templates.simple(request, title="Create Content", key=key, subtitle="In project")
    return HttpResponse(tpl)
