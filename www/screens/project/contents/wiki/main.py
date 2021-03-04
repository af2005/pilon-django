from django.http import HttpResponse

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
    project_descendants = Project.objects.filter(key=key).first().get_descendants()
    wiki_pages = WikiPage.objects.filter(id__in=project_descendants)
    context = {"nodes": wiki_pages}

    tpl = templates.project_view(
        request,
        key,
        template_name="www/project/wiki.html",
        title="",
        sidebar_items=main.sidebar_items(key),
        active_sidebar_item=6,
        additional_context=context
    )
    return HttpResponse(tpl)
