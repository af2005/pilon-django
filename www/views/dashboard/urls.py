from . import views
from django.urls import path

urlpatterns = [
    path("", views.dashboard, name="View Dashboard"),
    path(
        "dashboard/all-updates/",
        views.all_updates_board,
        name="All updates board",
    ),
    path(
        "dashboard/last-worked-on/",
        views.recently_worked_on_board,
        name="Last worked on board",
    ),
]
