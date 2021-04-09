from django.views.generic import UpdateView, DetailView, ListView, CreateView
from www.models import WikiPage
from ..views import ProjectContext


class WikiPageBase(ProjectContext):
    model = WikiPage
    fields = ["parent", "name", "markdown"]
    extra_context = {
        "active_sidebar_item": "Wiki"
    }


class WikiPageDetail(WikiPageBase, DetailView):
    template_name = "www/project/wiki/wiki_page_detail.html"


class WikiPageCreate(WikiPageBase, CreateView):
    template_name = "www/project/wiki/wiki_page_create.html"


class WikiPageCreateFromFile(WikiPageBase, CreateView):
    template_name = "www/project/wiki/wiki_page_create_from_file.html"


class WikiPageEdit(WikiPageBase, UpdateView):
    template_name = "www/project/wiki/wiki_page_edit.html"


class WikiHomepage(WikiPageBase, ListView):
    template_name = "www/project/wiki/wiki_home.html"
    extra_context = {
        "page_title": "Wiki Homepage"
    }
