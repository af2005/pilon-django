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


def view_wiki_homepage(request, key):
    tpl = templates.project_view(
        request,
        key,
        template_name="www/project/wiki_base.html",
        title="Wiki",
        sidebar_items=main.sidebar_items(key),
        active_sidebar_item=6,
        additional_context=get_page_tree(key)
    )
    return HttpResponse(tpl)


def view_wiki_page(request, key, uid):
    page_tree = get_page_tree(key)
    wiki_page = WikiPage.objects.filter(id=uid).first()
    ancestors = wiki_page.get_ancestors_of_type(WikiPage)
    page_contents = {
        "name": wiki_page.name,
        "content": wiki_page.markdown_rendered,
        "creator": wiki_page.creator,
        "created_date": wiki_page.date_created,
        "modified_date": wiki_page.date_modified,
        "ancestors": ancestors,
    }
    tpl = templates.project_view(
        request,
        key,
        template_name="www/project/wiki_page_view.html",
        title="",
        sidebar_items=main.sidebar_items(key),
        active_sidebar_item=6,
        additional_context={**page_tree, **page_contents}
    )
    return HttpResponse(tpl)


def get_page_tree(key):
    project_descendants = Project.objects.filter(key=key).first().get_descendants()
    wiki_pages = WikiPage.objects.filter(id__in=project_descendants)
    context = {"nodes": wiki_pages}
    return context
