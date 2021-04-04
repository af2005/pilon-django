from django.http import HttpResponse
from django.template import loader
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


def project_view(
    request,
    key,
    template,
    additional_context=None,
) -> HttpResponse:
    if additional_context is None:
        additional_context = {}
    project = (Project.objects.filter(key=key))[0]
    template = loader.get_template(template)
    context = {
        "project": project,
    }
    context = {**context, **additional_context}

    return HttpResponse(template.render(context, request))


def team(request, key) -> HttpResponse:
    return project_view(request, key, template="www/project/team/team_detail.html")


def chat(request, key) -> HttpResponse:
    return project_view(
        request,
        key,
        template="www/project/chat/chat_detail.html",
    )


def calendar(request, key) -> HttpResponse:
    return project_view(
        request,
        key,
        template="www/project/calendar/calendar_detail.html",
    )


def inventory(request, key) -> HttpResponse:
    return project_view(
        request,
        key,
        template="www/project/inventory/inventory_list.html",
    )
