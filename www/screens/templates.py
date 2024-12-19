from django.template import loader
from ..models import Project


def admin(request, window_title, title="", subtitle="", sidebar_items=None, content=None):
    template = loader.get_template('www/base+sidebar+title.html')
    context = {
        'window_title': window_title,
        'page_title': title,
        'page_subtitle': subtitle,
        'sidebar_items': sidebar_items,
        'content': content,
        'navbar_centertext': 'System settings',
    }
    return template.render(context, request)


def simple(request, window_title, title="", subtitle="", content="", navbar_centertext=""):
    template = loader.get_template('www/base+title.html')
    context = {
        'window_title': window_title,
        'content': content,
        'page_title': title,
        'page_subtitle': subtitle,
        'navbar_centertext': navbar_centertext,

    }
    return template.render(context, request)


def dashboard(request, window_title, title="", subtitle="", subnav_items=None, active_subnav_item=None, content=""):
    template = loader.get_template('www/dashboard/dashboard.html')
    context = {
        'window_title': window_title,
        'page_title': title,
        'page_subtitle': subtitle,
        'subnav_items': subnav_items,
        'active_subnav_item': active_subnav_item,
        'content': content
    }
    return template.render(context, request)


def people(request, window_title, title="", subtitle="", users=[]):
    template = loader.get_template('www/snippets/people.html')
    context = {
        'window_title': window_title,
        'page_title': title,
        'page_subtitle': subtitle,
        'users': users
    }
    return template.render(context, request)


def project_directory(request, projects=[]):
    template = loader.get_template('www/project/directory.html')
    context = {
        'window_title': "Project Directory",
        'page_title': "Project Directory",
        'page_subtitle': "All Projects visible to you",
        'projects': projects
    }
    return template.render(context, request)


def project_view(request, key, template_name, title, sidebar_items, active_sidebar_item):
    project = list(Project.objects.filter(key=key).values())[0]
    template = loader.get_template(template_name)
    context = {
        'project_key': project["key"],
        'window_title': f'{project["name"]} {title}',
        'page_title': f'{project["name"]} {title}',
        'page_subtitle': "",
        'project': project,
        'sidebar_items': sidebar_items,
        'navbar_centertext': project["name"],
        'active_sidebar_item': active_sidebar_item
    }
    return template.render(context, request)


def create_new_content(request, key, title, subtitle, sidebar_items):
    project = list(Project.objects.filter(key=key).values())[0]
    template = loader.get_template('www/project/create-content.html')
    context = {
        'project_key': project["key"],
        'window_title': f'{title} {project["name"]} ',
        'page_title': f'{title}',
        'page_subtitle': f'{subtitle} {project["name"]}',
        'project': project,
        'sidebar_items': sidebar_items,
        'navbar_centertext': project["name"],
    }
    return template.render(context, request)


def default_editor(request, key, title):
    project = list(Project.objects.filter(key=key).values())[0]
    template = loader.get_template('www/project/default-editor.html')
    context = {
        'project_key': project["key"],
        'window_title': f'{title} {project["name"]} ',
        'page_title': f'{title}',
        'project': project,
        'navbar_centertext': project["name"],
    }
    return template.render(context, request)



