import www.views.project.views as project_views


def overview(request, key):
    return project_views.project_view(request, key, template="tasks", title="Tasks", active_sidebar_item="Tasks")
