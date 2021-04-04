from django.http import HttpResponse

from www.models import JournalPage, Project
from www.views import templates
import www.views.project.views as project_views
from ..views import ProjectContext
from django.views.generic import UpdateView, DetailView, ListView, CreateView


def content_create_with_file(request, key) -> HttpResponse:
    tpl = templates.default_editor(request, title="Create Journal Page with File", key=key)
    return HttpResponse(tpl)


def homepage(request, key) -> HttpResponse:
    return project_views.project_view(
        request, key, template="www/project/journal/journal_page_list.html"
    )


def page(request, key, uuid) -> HttpResponse:
    # TODO: Do not return homepage but actual page
    return project_views.project_view(request, key, template="journal")


class JournalPageBase(ProjectContext):
    model = JournalPage
    fields = ["parent", "name", "markdown"]


class JournalHomepage(JournalPageBase, ListView):
    template_name = "www/project/journal/journal_page_list.html"


class JournalPageDetail(JournalPageBase, DetailView):
    template_name = "www/project/journal/journal_page_detail.html"


class JournalPageCreate(JournalPageBase, CreateView):
    template_name = "www/project/journal/journal_page_create.html"
