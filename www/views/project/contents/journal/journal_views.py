from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader, Template
from www.views.snippets import forms
from www.models import Project
from www.views import templates
from .. import project_content_views


@login_required
def view_content_create(request, key):
    tpl = templates.default_editor(request, title="Create Journal Page", key=key)
    return HttpResponse(tpl)


@login_required
def view_content_create_with_file(request, key):
    tpl = templates.default_editor(
        request, title="Create Journal Page with File", key=key
    )
    return HttpResponse(tpl)


@login_required
def view_journal(request, key):
    tpl = templates.project_view(
        request,
        key,
        template_name="www/project/journal.html",
        title="Journal",
        sidebar_items=project_content_views.sidebar_items(key),
        active_sidebar_item=7,
    )
    return HttpResponse(tpl)
