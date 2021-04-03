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


def _get_page_tree(key) -> dict:
    wiki_pages = (
        Project.objects.filter(key=key).first().get_descendants().instance_of(WikiPage)
    )
    context = {"nodes": wiki_pages}
    return context


def content_create_with_file(request, key) -> HttpResponse:
    tpl = templates.default_editor(request, title="Create Wiki Page with File", key=key)
    return HttpResponse(tpl)


class WikiPageDetail(ProjectContext, DetailView):
    model = WikiPage
    template_name = "www/project/wiki/wiki_page_detail.html"


class WikiPageCreate(CreateView):
    model = WikiPage
    fields = [
        "parent",
        "name",
    ]
    template_name = "www/project/wiki/wiki_page_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get("key")
        page_tree = _get_page_tree(key)
        project = list(Project.objects.filter(key=key))[0]
        normal_context = {
            "project": project,
        }
        context = {**context, **normal_context, **page_tree}
        return context


class WikiPageUpdate(UpdateView):
    model = WikiPage
    fields = ["name"]
    template_name = "www/project/wiki/wiki_page_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get("key")
        page_tree = _get_page_tree(key)
        project = list(Project.objects.filter(key=key))[0]
        page_contents = {
            "ancestors": self.object.get_ancestors_of_type(WikiPage),
            "project": project,
        }
        context = {**context, **page_tree, **page_contents}
        return context


class WikiHomepage(ListView):
    model = WikiPage
    template_name = "www/project/wiki/wiki_home.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get("key")
        page_tree = _get_page_tree(key)
        project = list(Project.objects.filter(key=key))[0]
        normal_context = {
            "project": project,
        }
        context = {**context, **normal_context, **page_tree}
        return context
