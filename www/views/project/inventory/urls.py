from django.urls import path
from .views import InventoryHome

urlpatterns = [
    path("", InventoryHome.as_view(), name="inventory"),
]
