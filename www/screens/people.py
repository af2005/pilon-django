from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import templates
from ..rest import users


@login_required
def directory(request):
    tpl = templates.people(request,
                           window_title="People",
                           title="People directory",
                           users=users.list_all_users())
    return HttpResponse(tpl)
