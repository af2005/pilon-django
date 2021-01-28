from django.http import HttpResponse
from django.template import loader


def view_create(request):
    template = loader.get_template('www/default-without-sidebar.html')
    context = {
        'window_title': "Create project",
        'page_title': "Create new project",
        'page_subtitle': "Every projects needs a key (consisting out of a few letters or numbers) and a name.",

    }
    return HttpResponse(template.render(context, request))


def view_directory(request):
    template = loader.get_template('www/default-without-sidebar.html')
    context = {
        'window_title': "Project directorys",
        'page_title': "Project Directory",
        'page_subtitle': "All Projects visible to you",
    }
    return HttpResponse(template.render(context, request))


def view_homepage(request):
    pass
