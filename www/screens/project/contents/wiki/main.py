from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader, Template
from www.screens.snippets import forms
from www.models import Project, Entity, WikiPage
from www.screens import templates
from .. import main


def view_content_create(request, key):
    tpl = templates.default_editor(request, title="Create Wiki Page", key=key)
    return HttpResponse(tpl)


def view_content_create_with_file(request, key):
    tpl = templates.default_editor(request, title="Create Wiki Page with File", key=key)
    return HttpResponse(tpl)


def view_wiki(request, key):
    tpl = templates.project_view(
        request,
        key,
        template_name="www/project/wiki.html",
        title="",
        sidebar_items=main.sidebar_items(key),
        active_sidebar_item=6,
    )
    return HttpResponse(tpl)


def test_page_tree(request, key):
    tpl = loader.get_template("www/project/wiki-tree-test.html")
    wiki_pages = Project.objects.filter(key=key).first().get_descendants().instance_of(WikiPage)
    context = {"nodes": wiki_pages}
    tpl = tpl.render(context, request)
    return HttpResponse(tpl)
