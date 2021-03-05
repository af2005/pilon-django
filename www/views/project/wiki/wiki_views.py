from django.http import HttpResponse

from www.models import Project, WikiPage
from www.views import templates
from .. import project_views


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
        sidebar_items=project_views.sidebar_items(key),
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
        "id": wiki_page.id,
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
        sidebar_items=project_views.sidebar_items(key),
        active_sidebar_item=6,
        additional_context={**page_tree, **page_contents}
    )
    return HttpResponse(tpl)


def get_page_tree(key):
    wiki_pages = Project.objects.filter(key=key).first().get_descendants().instance_of(WikiPage)
    context = {"nodes": wiki_pages}
    return context
