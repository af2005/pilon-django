from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .. import templates
from www.rest import users

SIDEBAR_ITEMS = [
    {'name': 'Global', 'url': '/system-settings/global'},
    {'name': 'User Manager', 'url': '/system-settings/user-manager'}
]


@login_required
def user_settings(request):
    return HttpResponse("User settings")


@login_required
@permission_required('admin', raise_exception=True)
def user_manager(request):
    content = users.list_all_users()
    tpl = templates.admin(request, "User Manager", title="Manage Users", sidebar_items=SIDEBAR_ITEMS,
                          content=content)
    return HttpResponse(tpl)


@login_required
@permission_required('admin', raise_exception=True)
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
