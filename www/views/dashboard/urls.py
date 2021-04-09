from django.urls import path
from .views import DashboardAllUpdates, DashboardLastWorkedOn, DashboardView

app_name = "dashboard"

urlpatterns = [
    path("", DashboardView.as_view(), name="home"),
    path(
        "dashboard/all-updates/",
        DashboardAllUpdates.as_view(),
        name="all-updates",
    ),
    path(
        "dashboard/last-worked-on/",
        DashboardLastWorkedOn.as_view(),
        name="last-worked-on",
    ),
]
