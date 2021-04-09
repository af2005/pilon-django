from django.views.generic import ListView, TemplateView
from ..views import ProjectContext


class InventoryBase(ProjectContext):
    active_sidebar_item = "Inventory"


class InventoryList(InventoryBase, TemplateView):
    template_name = "www/project/inventory/inventory_list.html"
    context_object_name = "inventory"


class InventoryHomepage(InventoryList):
    pass
