from django.http import HttpResponse

from www.views import templates
import www.views.project.views as project_views


def view_tasks(request, key):
    tpl = templates.project_view(
        request,
        key,
        template_name="www/project/tasks.html",
        title="Tasks",
        sidebar_items=project_views.sidebar_items(key),
        active_sidebar_item=3,
    )
    return HttpResponse(tpl)
