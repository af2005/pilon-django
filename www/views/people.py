from django.http import HttpResponse
from . import templates
from django.views.generic import ListView
from django.contrib.auth import get_user_model

User = get_user_model()


class PeopleDirectory(ListView):
    model = User
    template_name = "www/snippets/people.html"
    context_object_name = "users"


def directory(request):

    tpl = templates.people(
        request,
        window_title="People",
        title="People directory",
        users=User.objects.all(),
    )
    return HttpResponse(tpl)
