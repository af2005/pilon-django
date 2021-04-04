from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import ContextMixin, View

from www.models import Project
from www.views import templates
from django.urls import reverse


class ProjectContext(ContextMixin, View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get("key")
        context["project"] = Project.objects.filter(key=key).first()
        return context


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


def content_create(request, key) -> HttpResponse:
    tpl = templates.create_new_content(
        request,
        title="Create Content",
        key=key,
        subtitle="In project",
    )
    return HttpResponse(tpl)


def homepage(request, key) -> HttpResponse:
    return project_view(
        request,
        key,
        template="www/project/project_homepage.html",
    )


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
