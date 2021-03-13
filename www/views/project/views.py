from django.http import HttpResponse
from www.views import templates
from django.urls import reverse


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
            "color": "darkorange",
        },
        {
            "name": "Chat",
            "url": reverse('project:chat', args=[key]),
            "icon": "envelope",
            "color": "darkred",
        },
        {
            "name": "Tasks",
            "url": reverse('project:tasks', args=[key]),
            "icon": "check2-circle",
            "color": "indigo",
        },
        {
            "name": "Calendar",
            "url": reverse('project:calendar', args=[key]),
            "icon": "calendar3",
            "color": "pink",
        },
        {
            "name": "Inventory",
            "url": reverse('project:inventory', args=[key]),
            "icon": "archive",
            "color": "blue2",
        },
        {
            "name": "Wiki",
            "url": reverse('project:wiki', args=[key]),
            "icon": "file-text",
            "color": "darkred",
        },
        {
            "name": "Journal",
            "url": reverse('project:journal', args=[key]),
            "icon": "journals",
            "color": "darkteal",
        },
    ]


def view_content_create(request, key):
    tpl = templates.create_new_content(
        request,
        title="Create Content",
        key=key,
        subtitle="In project",
        sidebar_items=sidebar_items(key),
    )
    return HttpResponse(tpl)


def view_homepage(request, key):
    tpl = templates.project_view(
        request,
        key,
        template_name="www/project/homepage.html",
        title="Homepage",
        sidebar_items=sidebar_items(key),
        active_sidebar_item=0,
    )
    return HttpResponse(tpl)


def view_team(request, key):
    tpl = templates.project_view(
        request,
        key,
        template_name="www/project/team.html",
        title="Team",
        sidebar_items=sidebar_items(key),
        active_sidebar_item=1,
    )
    return HttpResponse(tpl)


def view_chat(request, key):
    tpl = templates.project_view(
        request,
        key,
        template_name="www/project/chat.html",
        title="Chat",
        sidebar_items=sidebar_items(key),
        active_sidebar_item=2,
    )
    return HttpResponse(tpl)


def view_calendar(request, key):
    tpl = templates.project_view(
        request,
        key,
        template_name="www/project/calendar.html",
        title="Calendar",
        sidebar_items=sidebar_items(key),
        active_sidebar_item=4,
    )
    return HttpResponse(tpl)


def view_inventory(request, key):
    tpl = templates.project_view(
        request,
        key,
        template_name="www/project/inventory.html",
        title="Inventory",
        sidebar_items=sidebar_items(key),
        active_sidebar_item=5,
    )
    return HttpResponse(tpl)


