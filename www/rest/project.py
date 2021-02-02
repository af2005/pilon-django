from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect

from ..models import Project


def rest_handler_all(request):
    if request.method == "GET":
        return get_all_projects()

    elif request.method == "POST":

        if request.POST["project_key"] and request.POST["project_fullname"]:
            create_new_project(request.POST["project_key"], request.POST["project_fullname"])
            return HttpResponseRedirect("/p/c/"+request.POST["project_key"])
        else:
            return HttpResponseBadRequest("You need to provide a key and a name when creating a new project")

    return HttpResponseBadRequest()


def get_all_projects():
    """
    :return: HTTPResponse with JSONObject of all project in the system
    """
    return HttpResponse(Project.objects.all())


def get_single_project(key):
    return repr(Project.objects.filter(key=key))


def create_new_project(key, name):
    """
    Creates a new project
    :param key: key of the new project
    :param name: name of the new project
    :return: void
    """
    project = Project(key=key, name=name)
    project.save()
