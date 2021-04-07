from django.views.generic import UpdateView, DetailView, ListView, CreateView
from ..views import ProjectContext
from www.models import Task


class InventoryBase(ProjectContext):
    model = Task
    fields = []


class InventoryList(InventoryBase, ListView):
    template_name = "www/project/tasks/task_list.html"
    context_object_name = "tasks"


class InventoryHomepage(InventoryList):
    pass
