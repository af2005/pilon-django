from django.template import loader
from ..models import Project


def admin(
    request, window_title, title="", subtitle="", sidebar_items=None, content=None
):
    template = loader.get_template("www/base/base+sidebar+title.html")
    context = {
        "window_title": window_title,
        "page_title": title,
        "page_subtitle": subtitle,
        "sidebar_items": sidebar_items,
        "content": content,
        "navbar_centertext": "System settings",
    }
    return template.render(context, request)


def simple(
    request, window_title, title="", subtitle="", content="", navbar_centertext=""
):
    template = loader.get_template("www/base/base+title.html")
    context = {
        "window_title": window_title,
        "content": content,
        "page_title": title,
        "page_subtitle": subtitle,
        "navbar_centertext": navbar_centertext,
    }
    return template.render(context, request)


def dashboard(
    request,
    window_title,
    title="",
    subtitle="",
    subnav_items=None,
    active_subnav_item=None,
    content="",
):
    template = loader.get_template("www/dashboard/dashboard.html")
    context = {
        "window_title": window_title,
        "page_title": title,
        "page_subtitle": subtitle,
        "subnav_items": subnav_items,
        "active_subnav_item": active_subnav_item,
        "content": content,
    }
    return template.render(context, request)


def people(request, window_title, title="", subtitle="", users=None):
    if users is None:
        users = []
    template = loader.get_template("www/snippets/people.html")
    context = {
        "window_title": window_title,
        "page_title": title,
        "page_subtitle": subtitle,
        "users": users,
    }
    return template.render(context, request)


def project_directory(request, projects=None):
    if projects is None:
        projects = []
    template = loader.get_template("www/project/project_list.html")
    context = {
        "window_title": "Project Directory",
        "page_title": "Project Directory",
        "page_subtitle": "All Projects visible to you",
        "projects": projects,
    }
    return template.render(context, request)


def default_editor(request, key, title):
    project = list(Project.objects.filter(key=key).values())[0]
    template = loader.get_template("www/project/wiki/wiki_page_create.html")
    context = {
        "project_key": project["key"],
        "window_title": f'{title} {project["name"]} ',
        "page_title": f"{title}",
        "project": project,
        "navbar_centertext": project["name"],
    }
    return template.render(context, request)
