import www.views.project.views as project_views


def overview(request, key):
    return project_views.project_view(
        request, key, template="www/project/tasks/task_list.html"
    )
