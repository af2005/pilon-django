from django.urls import path
from .views import DashboardAllUpdates, DashboardLastWorkedOn, DashboardView

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard-view"),
    path(
        "dashboard/all-updates/",
        DashboardAllUpdates.as_view(),
        name="dashboard-all-updates",
    ),
    path(
        "dashboard/last-worked-on/",
        DashboardLastWorkedOn.as_view(),
        name="dashboard-last-worked-on",
    ),
]
