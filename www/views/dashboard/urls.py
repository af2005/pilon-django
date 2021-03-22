from . import dashboard_views
from django.urls import path

urlpatterns = [
    path("", dashboard_views.view_dashboard, name="View Dashboard"),
    path(
        "dashboard/all-updates/",
        dashboard_views.view_all_updates_board,
        name="All updates board",
    ),
    path(
        "dashboard/last-worked-on/",
        dashboard_views.view_recently_worked_on_board,
        name="Last worked on board",
    ),
]
