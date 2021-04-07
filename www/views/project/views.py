from django.views.generic.base import ContextMixin, View
from django.views.generic import ListView, CreateView, TemplateView

from www.models import Project


class ProjectContext(ContextMixin, View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get("key")
        context["project"] = Project.objects.filter(key=key).first()
        return context


class ProjectHomepage(ProjectContext, TemplateView):
    template_name = "www/project/project_homepage.html"


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
