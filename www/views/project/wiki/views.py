from django.http import HttpResponse
from django.views.generic import UpdateView, DetailView, ListView, CreateView

from www.models import Project, WikiPage
from www.views import templates
import www.views.project.views as project_views


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


def page(request, key, uuid) -> HttpResponse:
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
    return project_views.project_view(
        request,
        key,
        template="wiki/page_view",
        title="",
        additional_context={**page_tree, **page_contents},
    )


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
    # success_url = "/"
    title = "Wiki Page Create"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get("key")
        page_tree = _get_page_tree(key)
        active_sidebar_item = "Wiki"
        project = list(Project.objects.filter(key=key))[0]
        normal_context = {
            "project_key": key,
            "window_title": f"{project.name} {self.title}",
            "page_title": self.title,
            "page_subtitle": "",
            "project": project,
            "parent": project.id,  # TODO: check how to give the parent
            "navbar_centertext": project.name,
            "active_sidebar_item": active_sidebar_item,
        }
        context = {**context, **normal_context, **page_tree}
        return context


class WikiPageUpdate(UpdateView):
    model = WikiPage
    fields = ["name"]
    template_name = "www/project/wiki/wiki_page_update.html"
    # success_url = "/"
    title = "Wiki Page Update"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get("key")
        page_tree = _get_page_tree(key)
        wikipage = self.object
        print(wikipage._meta.model_name)
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
        active_sidebar_item = "Wiki"
        project = list(Project.objects.filter(key=key))[0]
        normal_context = {
            "project_key": key,
            "window_title": f"{project.name} {self.title}",
            "page_title": self.title,
            "page_subtitle": "",
            "project": project,
            "navbar_centertext": project.name,
            "active_sidebar_item": active_sidebar_item,
        }
        context = {**context, **normal_context, **page_tree, **page_contents}
        return context


class WikiHomepage(ListView):
    model = WikiPage
    template_name = "www/project/wiki/wiki_home.html"
    title = "Wiki Home"

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
