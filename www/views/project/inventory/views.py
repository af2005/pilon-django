from django.views.generic import UpdateView, DetailView, ListView, CreateView
from ..views import ProjectContext
from www.models import Task


class TaskBase(ProjectContext):
    model = Task
    fields = ["parent", "name", "assignee"]


class TaskDetail(TaskBase, DetailView):
    model = Task
    template_name = "www/project/tasks/task_detail.html"


class TaskCreate(TaskBase, CreateView):
    template_name = "www/project/tasks/task_create.html"


class TaskEdit(TaskBase, UpdateView):
    template_name = "www/project/tasks/task_edit.html"


class TaskList(TaskBase, ListView):
    template_name = "www/project/tasks/task_list.html"
    context_object_name = "tasks"


class TaskHomepage(TaskList):
    pass
