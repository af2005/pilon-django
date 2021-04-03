from django.http import HttpResponse
from django.views.generic import UpdateView, DetailView, ListView, CreateView, View
from django.views.generic.base import ContextMixin

from www.models import Project, WikiPage
from www.views import templates


class ProjectContext(ContextMixin, View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get("key")
        context["project"] = Project.objects.filter(key=key).first()
        return context


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
    fields = ["name"]
    template_name = "www/project/wiki/wiki_page_edit.html"


class WikiHomepage(ProjectContext, ListView):
    model = WikiPage
    template_name = "www/project/wiki/wiki_home.html"
