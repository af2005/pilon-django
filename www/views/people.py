from django.http import HttpResponse
from . import templates
from www.models import User


def directory(request):

    tpl = templates.people(
        request,
        window_title="People",
        title="People directory",
        users=User.objects.all(),
    )
    return HttpResponse(tpl)
