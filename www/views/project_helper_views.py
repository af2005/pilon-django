from django.http import HttpResponse
from django.template import loader
from www.models import Project
from www.views import templates


def view_project_create(request):
    template = loader.get_template("www/project/create/project.html")
    context = {
        "window_title": "Create project",
        "page_title": "Create new project",
        "page_subtitle": "Every projects needs a key (consisting out of a few letters or numbers) and a name.",
        "content": "",
    }

    return HttpResponse(template.render(context, request))


def view_directory(request):
    tpl = templates.project_directory(request, projects=Project.objects.all())
    return HttpResponse(tpl)
