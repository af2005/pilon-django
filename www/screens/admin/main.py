from django.http import HttpResponse
from django.template import loader
from .. import templates
from www.rest import users

SIDEBAR_ITEMS = [
    {'name': 'Global', 'url': 'global'},
    {'name': 'User Manager', 'url': 'user-manager'}
]


def user_settings(request):
    return HttpResponse("User settings")


def user_manager(request):
    content = users.list_all_users()
    tpl = templates.admin(request, "User Manager", title="Manage Users", sidebar_items=SIDEBAR_ITEMS,
                          content=content)
    return HttpResponse(tpl)


def system_settings(request, setting):
    if setting == "user-manager":
        return user_manager(request)

    content = ""
    tpl = templates.admin(request,
                          window_title="System Settings",
                          title=setting,
                          sidebar_items=SIDEBAR_ITEMS,
                          content=content)
    return HttpResponse(tpl)
