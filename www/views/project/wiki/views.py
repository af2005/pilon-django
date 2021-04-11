from django.views.generic import UpdateView, DetailView, ListView, CreateView
from www.models.models import WikiPage
from ..views import ProjectContext


class WikiPageBase(ProjectContext):
    model = WikiPage
    active_sidebar_item = "Wiki"
    extra_context = {"page_title": ""}
    fields = ["parent", "name", "markdown"]


class WikiPageDetail(WikiPageBase, DetailView):
    template_name = "www/project/wiki/wiki_page_detail.html"


class WikiPageCreate(WikiPageBase, CreateView):
    template_name = "www/project/wiki/wiki_page_create.html"
    extra_context = {"page_title": "Create Wiki Page"}


class WikiPageCreateFromFile(WikiPageBase, CreateView):
    template_name = "www/project/wiki/wiki_page_create_from_file.html"


class WikiPageEdit(WikiPageBase, UpdateView):
    template_name = "www/project/wiki/wiki_page_edit.html"


class WikiHome(WikiPageBase, ListView):
    template_name = "www/project/wiki/wiki_home.html"
    extra_context = {"page_title": "Wiki Home"}
