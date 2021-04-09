from django.contrib.auth.decorators import permission_required
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.template import loader

User = get_user_model()

SIDEBAR_ITEMS = [
    {"name": "Global", "url": "/system-settings/global"},
    {"name": "User Manager", "url": "/system-settings/user-manager"},
]


def template_admin(request, window_title, title="", subtitle="", sidebar_items=None, content=None):
    template = loader.get_template("www/base/base+sidebar+title.html")
    context = {
        "window_title": window_title,
        "page_title": title,
        "page_subtitle": subtitle,
        "sidebar_items": sidebar_items,
        "content": content,
        "navbar_centertext": "System settings",
    }
    return template.render(context, request)


def user_settings(request):
    return HttpResponse("User settings")


@permission_required("admin", raise_exception=True)
def user_manager(request):
    content = User.objects.all()
    tpl = template_admin(
        request,
        "User Manager",
        title="Manage Users",
        sidebar_items=SIDEBAR_ITEMS,
        content=content,
    )
    return HttpResponse(tpl)


@permission_required("admin", raise_exception=True)
def system_settings(request, setting):
    if setting == "user-manager":
        return user_manager(request)

    content = ""
    tpl = template_admin(
        request,
        window_title="System Settings",
        title=setting,
        sidebar_items=SIDEBAR_ITEMS,
        content=content,
    )
    return HttpResponse(tpl)
