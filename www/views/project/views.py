from django.http import HttpResponse
from django.template import loader

from www.models import Project
from www.views import templates
from django.urls import reverse


def project_view(
        request,
        key,
        template,
        title,
        additional_context=None,
) -> HttpResponse:
    if additional_context is None:
        additional_context = {}
    project = (Project.objects.filter(key=key))[0]
    template = loader.get_template(f"www/project/content/{template}.html")
    context = {
        "window_title": f'{project.name} {title}',
        "page_title": title,
        "page_subtitle": "",
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
        template="homepage",
        title="Homepage",
    )


def team(request, key) -> HttpResponse:
    return project_view(
        request, key, template="team", title="Team", )


def chat(request, key) -> HttpResponse:
    return project_view(
        request, key, template="chat", title="Chat",
    )


def calendar(request, key) -> HttpResponse:
    return project_view(
        request,
        key,
        template="calendar",
        title="Calendar",
    )


def inventory(request, key) -> HttpResponse:
    return project_view(
        request,
        key,
        template="inventory",
        title="Inventory",
    )
