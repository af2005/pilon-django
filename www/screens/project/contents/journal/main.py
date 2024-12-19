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
        request, title="Create Journal Page", key=key,
    )
    return HttpResponse(tpl)


@login_required
def view_journal(request, key):
    tpl = templates.project_view(request, key, template_name="www/project/journal.html", title="Journal",
                                 sidebar_items=main.sidebar_items(key),
                                 active_sidebar_item=7)
    return HttpResponse(tpl)
