from django.views.generic import UpdateView, DetailView, ListView, CreateView
from ..views import ProjectContext
from www.models import Task


class InventoryBase(ProjectContext):
    model = Task
    fields = []


class InventoryList(InventoryBase, ListView):
    template_name = "www/project/inventory/inventory_list.html"
    context_object_name = "inventory"
    extra_context = {
        "active_sidebar_item": "Inventory",
        "page_title": "Inventory",
        "window_title": "Inventory"
    }


class InventoryHomepage(InventoryList):
    pass
