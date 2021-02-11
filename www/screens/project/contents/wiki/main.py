from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader, Template
from www.screens.snippets import forms
from www.models import Project
from www.screens import templates
from .. import main


@login_required
def view_content_create(request, key):
    tpl = templates.default_editor(
        request,
        title="Create Wiki Page",
        key=key,
    )
    return HttpResponse(tpl)


@login_required
def view_content_create_with_file(request, key):
    tpl = templates.default_editor(
        request,
        title="Create Wiki Page with File",
        key=key,
    )
    return HttpResponse(tpl)


@login_required
def view_wiki(request, key):
    tpl = templates.project_view(
        request,
        key,
        template_name="www/project/wiki.html",
        title="Wiki",
        sidebar_items=main.sidebar_items(key),
        active_sidebar_item=6,
    )
    return HttpResponse(tpl)
