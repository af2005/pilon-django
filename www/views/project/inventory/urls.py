from django.urls import path
from .views import InventoryHomepage

urlpatterns = [
    path("", InventoryHomepage.as_view(), name="inventory"),
]
