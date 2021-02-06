from django.http import HttpResponse
from www.screens import templates
from django.contrib.auth.decorators import login_required

SUBNAV_ITEMS = [
    {
        'name': "Dashboard",
        'url': "/",
    },
    {
        'name': "All updates",
        'url': "/dashboard/all-updates",
    },
    {
        'name': "Last worked on",
        'url': "/dashboard/last-worked-on",
    }
]


@login_required
def view_dashboard(request):
    tpl = templates.dashboard(request,
                              window_title="Dashboard",
                              title="Today",
                              subnav_items=SUBNAV_ITEMS,
                              active_subnav_item=0
                              )

    return HttpResponse(tpl)


@login_required
def view_all_updates_board(request):
    tpl = templates.dashboard(request,
                              window_title="All updates",
                              title="All updates",
                              subnav_items=SUBNAV_ITEMS,
                              active_subnav_item=1
                              )

    return HttpResponse(tpl)


@login_required
def view_recently_worked_on_board(request):
    tpl = templates.dashboard(request,
                              window_title="Recently worked on",
                              title="Recently worked on",
                              subnav_items=SUBNAV_ITEMS,
                              active_subnav_item=2
                              )

    return HttpResponse(tpl)
