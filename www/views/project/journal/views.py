from django.http import HttpResponse

from www.views import templates
import www.views.project.views as project_views


def content_create(request, key) -> HttpResponse:
    tpl = templates.default_editor(request, title="Create Journal Page", key=key)
    return HttpResponse(tpl)


def content_create_with_file(request, key) -> HttpResponse:
    tpl = templates.default_editor(
        request, title="Create Journal Page with File", key=key
    )
    return HttpResponse(tpl)


def homepage(request, key) -> HttpResponse:
    return project_views.project_view(request, key, template="journal", title="Journal", active_sidebar_item="Journal")


def page(request, key, uuid) -> HttpResponse:
    # TODO: Do not return homepage but actual page
    return project_views.project_view(request, key, template="journal", title="Journal", active_sidebar_item="Journal")
