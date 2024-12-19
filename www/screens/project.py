from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader, Template
from .snippets import forms
from ..models import Project
from . import templates


def sidebar_items(key):
    return [
        {
            'name': "Homepage",
            'url': f"/project/contents/{key}",
            'icon': 'house'
        },
        {
            'name': "Team",
            'url': f"/project/contents/{key}/team",
            'icon': 'people-fill'
        },
        {
            'name': "Chat",
            'url': f"/project/contents/{key}/chat",
            'icon': 'envelope'
        },
        {
            'name': "Tasks",
            'url': f"/project/contents/{key}/tasks",
            'icon': 'check2-circle'
        },
        {
            'name': "Calendar",
            'url': f"/project/contents/{key}/calendar",
            'icon': 'calendar3'
        },
        {
            'name': "Inventory",
            'url': f"/project/contents/{key}/inventory",
            'icon': 'archive'
        },
        {
            'name': "Wiki",
            'url': f"/project/contents/{key}/wiki",
            'icon': 'file-text'
        },
        {
            'name': "Journal",
            'url': f"/project/contents/{key}/journal",
            'icon': 'journals'
        }
    ]


@login_required
def view_project_create(request):
    template = loader.get_template('www/project/create.html')
    context = {
        'window_title': "Create project",
        'page_title': "Create new project",
        'page_subtitle': "Every projects needs a key (consisting out of a few letters or numbers) and a name.",
        'content': ""
    }

    return HttpResponse(template.render(context, request))


@login_required
def view_directory(request):
    tpl = templates.project_directory(request, projects=Project.objects.all())
    return HttpResponse(tpl)


@login_required
def view_homepage(request, key):
    tpl = templates.project_view(request, key, template_name="www/project/homepage.html", title="Homepage",
                                 sidebar_items=sidebar_items(key),
                                 active_sidebar_item=0)
    return HttpResponse(tpl)


@login_required
def view_team(request, key):
    tpl = templates.project_view(request, key, template_name="www/project/team.html", title="Team",
                                 sidebar_items=sidebar_items(key),
                                 active_sidebar_item=1)
    return HttpResponse(tpl)


@login_required
def view_chat(request, key):
    tpl = templates.project_view(request, key, template_name="www/project/chat.html", title="Chat",
                                 sidebar_items=sidebar_items(key),
                                 active_sidebar_item=2)
    return HttpResponse(tpl)


@login_required
def view_tasks(request, key):
    tpl = templates.project_view(request, key, template_name="www/project/tasks.html", title="Tasks",
                                 sidebar_items=sidebar_items(key),
                                 active_sidebar_item=3)
    return HttpResponse(tpl)


@login_required
def view_calendar(request, key):
    tpl = templates.project_view(request, key, template_name="www/project/calendar.html", title="Calendar",
                                 sidebar_items=sidebar_items(key),
                                 active_sidebar_item=4)
    return HttpResponse(tpl)


@login_required
def view_inventory(request, key):
    tpl = templates.project_view(request, key, template_name="www/project/inventory.html", title="Inventory",
                                 sidebar_items=sidebar_items(key),
                                 active_sidebar_item=5)
    return HttpResponse(tpl)


@login_required
def view_wiki(request, key):
    tpl = templates.project_view(request, key, template_name="www/project/wiki.html", title="Wiki",
                                 sidebar_items=sidebar_items(key),
                                 active_sidebar_item=6)
    return HttpResponse(tpl)


@login_required
def view_journal(request, key):
    tpl = templates.project_view(request, key, template_name="www/project/journal.html", title="Journal",
                                 sidebar_items=sidebar_items(key),
                                 active_sidebar_item=7)
    return HttpResponse(tpl)
