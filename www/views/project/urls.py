from django.urls import path, include
from . import project_views

urlpatterns = [
    path("<str:key>/", project_views.view_homepage, name="Project Homepage"),
    path("<str:key>/create/", project_views.view_content_create, name="Create Content"),
    path("<str:key>/team/", project_views.view_team, name="Project Team"),
    path("<str:key>/chat/", project_views.view_chat, name="Project Chat"),
    path("<str:key>/tasks/", project_views.view_tasks, name="Project Tasks"),
    path("<str:key>/calendar/", project_views.view_calendar, name="Project Calendar"),
    path("<str:key>/inventory/", project_views.view_inventory, name="Project Inventory"),
    path("<str:key>/wiki/", include("www.views.project.wiki.urls")),
    path("<str:key>/journal/", include("www.views.project.journal.urls")),
]