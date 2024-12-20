from django.views.generic.base import ContextMixin, View
from django.views.generic import ListView, CreateView, TemplateView

from www.models.entity import Project


class ProjectContext(ContextMixin, View):
    active_sidebar_item = None
    query_pk_and_slug = True
    slug_url_kwarg = "id"
    slug_field = "id"

    def get_context_data(self, **kwargs):
        key = self.kwargs.get("key")
        context = {"project": Project.objects.filter(key=key).first()}
        self.set_sidebar_context(context)
        return super().get_context_data(
            **{**kwargs, **context}
        )  # like this, the extra_context is added last

    def set_sidebar_context(self, context):
        context["active_sidebar_item"] = self.active_sidebar_item
        context["window_title"] = self.active_sidebar_item
        context["page_title"] = self.active_sidebar_item


class ProjectHome(ProjectContext, TemplateView):
    model = Project
    fields = ["name", "key"]
    template_name = "www/project/project_home.html"
    active_sidebar_item = "Home"
    extra_context = {
        "page_title": ""
    }


class ProjectCreate(CreateView):
    model = Project
    fields = ["name", "key"]
    template_name = "www/project/project_create.html"


class ProjectList(ListView):
    model = Project
    template_name = "www/project/project_list.html"
    context_object_name = "projects"


class ContentCreate(ProjectContext, TemplateView):
    template_name = "www/project/create_chooser.html"
