from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from ..models import Project
from django.contrib.auth.models import User
from schedule.models import Calendar


def rest_handler_all(request):
    if request.method == "GET":
        return get_all_projects()

    elif request.method == "POST":

        if request.POST["project_key"] and request.POST["project_fullname"]:
            create_new_project(
                request.user,
                request.POST["project_key"],
                request.POST["project_fullname"],
            )
            return HttpResponseRedirect("/p/c/" + request.POST["project_key"])
        else:
            return HttpResponseBadRequest(
                "You need to provide a key and a name when creating a new project"
            )

    return HttpResponseBadRequest()


def get_all_projects() -> HttpResponse:
    """
    :return: HTTPResponse with JSONObject of all project in the system
    """
    return HttpResponse(Project.objects.all())


def get_single_project(key: str) -> HttpResponse:
    return HttpResponse(Project.objects.filter(key=key))


def create_new_project(creator: User, key: str, name: str):
    """
    Creates a new project
    :param key: key of the new project
    :param name: name of the new project
    :return: void
    """
    project = Project(creator=creator, key=key, name=name)
    project.save()

    # add a calendar for this project
    try:
        cal = Calendar.objects.get(slug=key)

    except Calendar.DoesNotExist:
        cal = Calendar(name=name, slug=key)
        cal.save()
