
from django.http import HttpResponse
from . import templates
from django.contrib.auth.decorators import login_required

SIDEBAR_ITEMS = [
    {
        'name': "Latest updates",
        'url': "#"
    }
]


@login_required
def view_dashboard(request):
    tpl = templates.dashboard(request,
                              window_title="Dashboard",
                              title="Today",
                              sidebar_items=SIDEBAR_ITEMS
                              )

    return HttpResponse(tpl)
