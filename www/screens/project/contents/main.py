from django.http import HttpResponse, HttpResponseBadRequest
from www.screens import templates


def sidebar_items(key):
    return [
        {"name": "Homepage", "url": f"/p/c/{key}", "icon": "house"},
        {"name": "Team", "url": f"/p/c/{key}/team", "icon": "people-fill"},
        {"name": "Chat", "url": f"/p/c/{key}/chat", "icon": "envelope"},
        {"name": "Tasks", "url": f"/p/c/{key}/tasks", "icon": "check2-circle"},
        {"name": "Calendar", "url": f"/p/c/{key}/calendar", "icon": "calendar3"},
        {"name": "Inventory", "url": f"/p/c/{key}/inventory", "icon": "archive"},
        {"name": "Wiki", "url": f"/p/c/{key}/wiki", "icon": "file-text"},
        {"name": "Journal", "url": f"/p/c/{key}/journal", "icon": "journals"},
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


def view_tasks(request, key):
    tpl = templates.project_view(
        request,
        key,
        template_name="www/project/tasks.html",
        title="Tasks",
        sidebar_items=sidebar_items(key),
        active_sidebar_item=3,
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


def view_wiki(request, key):
    tpl = templates.project_view(
        request,
        key,
        template_name="www/project/wiki.html",
        title="Wiki",
        sidebar_items=sidebar_items(key),
        active_sidebar_item=6,
    )
    return HttpResponse(tpl)


def view_journal(request, key):
    tpl = templates.project_view(
        request,
        key,
        template_name="www/project/journal.html",
        title="Journal",
        sidebar_items=sidebar_items(key),
        active_sidebar_item=7,
    )
    return HttpResponse(tpl)
