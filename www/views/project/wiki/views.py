from django.http import HttpResponse
from django.views.generic import UpdateView, DetailView, ListView, CreateView

from www.models import WikiPage
from www.views import templates
from ..views import ProjectContext


def content_create_with_file(request, key) -> HttpResponse:
    tpl = templates.default_editor(request, title="Create Wiki Page with File", key=key)
    return HttpResponse(tpl)


class WikiPageDetail(ProjectContext, DetailView):
    model = WikiPage
    template_name = "www/project/wiki/wiki_page_detail.html"


class WikiPageCreate(ProjectContext, CreateView):
    model = WikiPage
    fields = [
        "parent",
        "name",
    ]
    template_name = "www/project/wiki/wiki_page_create.html"


class WikiPageEdit(ProjectContext, UpdateView):
    model = WikiPage
    fields = ["name", "markdown"]
    template_name = "www/project/wiki/wiki_page_edit.html"


class WikiHomepage(ProjectContext, ListView):
    model = WikiPage
    template_name = "www/project/wiki/wiki_home.html"
