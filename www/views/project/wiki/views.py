from django.http import HttpResponse
from django.views.generic import UpdateView, DetailView, ListView, CreateView

from www.models import WikiPage
from www.views import templates
from ..views import ProjectContext


def content_create_with_file(request, key) -> HttpResponse:
    tpl = templates.default_editor(request, title="Create Wiki Page with File", key=key)
    return HttpResponse(tpl)


class WikiPageBase(ProjectContext):
    model = WikiPage
    fields = ["parent", "name", "markdown"]


class WikiPageDetail(WikiPageBase, DetailView):
    model = WikiPage
    template_name = "www/project/wiki/wiki_page_detail.html"


class WikiPageCreate(WikiPageBase, CreateView):
    template_name = "www/project/wiki/wiki_page_create.html"


class WikiPageCreateFromFile(WikiPageBase, CreateView):
    template_name = "www/project/wiki/wiki_page_create_from_file.html"


class WikiPageEdit(WikiPageBase, UpdateView):
    template_name = "www/project/wiki/wiki_page_edit.html"


class WikiHomepage(WikiPageBase, ListView):
    template_name = "www/project/wiki/wiki_home.html"
