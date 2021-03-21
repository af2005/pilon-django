from django.http import HttpResponse
from django.template import loader

from www.models import Project
from www.views import templates
from django.urls import reverse


class ProjectComponent:
    def __init__(self, key, sidebar_index, name, icon, url_lookup, template):
        self.key = key
        self.sidebar_index = sidebar_index
        self.name = name
        self.icon = icon
        self.url_lookup = url_lookup
        self.template = template

    def template_path(self):
        return "www/project/" + self.template

    def url(self):
        return reverse('project:' + self.url_lookup, args=[self.key])


'''
homepage = ProjectComponent(sidebar_index=10, name="Homepage", icon="house-fill", url_lookup="homepage",
                            template="homepage")
team = ProjectComponent(sidebar_index=20, name="Team", icon="house-fill", url_lookup="project:homepage")
chat = ProjectComponent(sidebar_index=30, name="Chat", icon="house-fill", url_lookup="project:homepage")
tasks = ProjectComponent(sidebar_index=40, name="Tasks", icon="house-fill", url_lookup="project:homepage")
calendar = ProjectComponent(sidebar_index=50, name="", icon="house-fill", url_lookup="project:homepage")
inventory = ProjectComponent(sidebar_index=60, name="Tasks", icon="house-fill", url_lookup="project:homepage")
wiki = ProjectComponent(sidebar_index=70, name="Tasks", icon="house-fill", url_lookup="project:homepage")
journal = ProjectComponent(sidebar_index=80, name="Tasks", icon="house-fill", url_lookup="project:homepage")
'''


def sidebar_items(key):
    return [
        {
            "name": "Homepage",
            "url": reverse('project:homepage', args=[key]),
            "icon": "house-fill",
        },

        {
            "name": "Team",
            "url": reverse('project:team', args=[key]),
            "icon": "people",
        },
        {
            "name": "Chat",
            "url": reverse('project:chat', args=[key]),
            "icon": "envelope",
        },
        {
            "name": "Tasks",
            "url": reverse('project:tasks', args=[key]),
            "icon": "check2-circle",
        },
        {
            "name": "Calendar",
            "url": reverse('project:calendar', args=[key]),
            "icon": "calendar3",
        },
        {
            "name": "Inventory",
            "url": reverse('project:inventory', args=[key]),
            "icon": "archive",
        },
        {
            "name": "Wiki",
            "url": reverse('project:wiki', args=[key]),
            "icon": "file-text",
        },
        {
            "name": "Journal",
            "url": reverse('project:journal', args=[key]),
            "icon": "journals",
        },
    ]


def project_view(
        request, key, template, title, additional_context=None, active_sidebar_item=None,
):
    if additional_context is None:
        additional_context = {}
    project = list(Project.objects.filter(key=key).values())[0]
    template = loader.get_template(f"www/project/{template}.html")
    context = {
        "project_key": key,
        "window_title": f'{project["name"]} {title}',
        "page_title": title,
        "page_subtitle": "",
        "project": project,
        "sidebar_items": sidebar_items(key),
        "navbar_centertext": project["name"],
        "active_sidebar_item": active_sidebar_item,
    }
    context = {**context, **additional_context}

    return HttpResponse(template.render(context, request))


def content_create(request, key):
    tpl = templates.create_new_content(
        request, title="Create Content", key=key, subtitle="In project", sidebar_items=sidebar_items(key),
    )
    return HttpResponse(tpl)


def homepage(request, key):
    return project_view(request, key, template="homepage", title="Homepage", active_sidebar_item="Homepage")


def team(request, key):
    return project_view(request, key, template="team", title="Team", active_sidebar_item="Team")


def chat(request, key):
    return project_view(request, key, template="chat", title="Chat", active_sidebar_item="Chat")


def calendar(request, key):
    return project_view(request, key, template="calendar", title="Calendar", active_sidebar_item="Calendar")


def inventory(request, key):
    return project_view(request, key, template="inventory", title="Inventory", active_sidebar_item="Inventory")

