from django.http import HttpResponse
from django.views.generic import UpdateView, DetailView, ListView, CreateView

from www.models import Project, WikiPage
from www.views import templates


def _get_page_tree(key) -> dict:
    wiki_pages = (
        Project.objects.filter(key=key).first().get_descendants().instance_of(WikiPage)
    )
    context = {"nodes": wiki_pages}
    return context


def content_create(request, key) -> HttpResponse:
    tpl = templates.default_editor(request, title="Create Wiki Page", key=key)
    return HttpResponse(tpl)


def content_create_with_file(request, key) -> HttpResponse:
    tpl = templates.default_editor(request, title="Create Wiki Page with File", key=key)
    return HttpResponse(tpl)


class WikiPageDetail(DetailView):
    model = WikiPage
    template_name = "www/project/wiki/wiki_page_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get("key")
        page_tree = _get_page_tree(key)
        ancestors = self.object.get_ancestors_of_type(WikiPage)
        project = list(Project.objects.filter(key=key))[0]

        page_context = {
            "ancestors": ancestors,
            "project": project,
        }

        context = {**context, **page_context, **page_tree}
        return context


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
