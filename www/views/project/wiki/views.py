from django.http import HttpResponse

from www.models import Project, WikiPage
from www.views import templates
import www.views.project.views as project_views


def content_create(request, key):
    tpl = templates.default_editor(request, title="Create Wiki Page", key=key)
    return HttpResponse(tpl)


def content_create_with_file(request, key):
    tpl = templates.default_editor(request, title="Create Wiki Page with File", key=key)
    return HttpResponse(tpl)


def wiki_homepage(request, key):
    return project_views.project_view(request, key, template="wiki_base", title="Wiki",
                                      additional_context=_get_page_tree(key), active_sidebar_item="Wiki")


def page(request, key, uuid):
    page_tree = _get_page_tree(key)
    wikipage = WikiPage.objects.filter(id=uuid).first()
    ancestors = wikipage.get_ancestors_of_type(WikiPage)
    page_contents = {
        "name": wikipage.name,
        "id": wikipage.id,
        "content": wikipage.markdown_rendered,
        "creator": wikipage.creator,
        "created_date": wikipage.date_created,
        "modified_date": wikipage.date_modified,
        "ancestors": ancestors,
    }
    return project_views.project_view(request, key, template="wiki_page_view", title="",
                                      additional_context={**page_tree, **page_contents}, active_sidebar_item="Wiki"
                                      )


def _get_page_tree(key):
    wiki_pages = Project.objects.filter(key=key).first().get_descendants().instance_of(WikiPage)
    context = {"nodes": wiki_pages}
    return context
