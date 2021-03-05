from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import templates


@login_required
def main(request):
    tpl = templates.simple(
        request,
        window_title="User settings",
        title="User settings",
        navbar_centertext="User settings",
    )

    return HttpResponse(tpl)
