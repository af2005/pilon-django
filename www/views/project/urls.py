from django.urls import path, include
from . import project_views
app_name="project"

urlpatterns = [
    path("<str:key>/", project_views.view_homepage, name="homepage"),
    path("<str:key>/create/", project_views.view_content_create, name="create-child-entity"),
    path("<str:key>/team/", project_views.view_team, name="team"),
    path("<str:key>/chat/", project_views.view_chat, name="chat"),
    path("<str:key>/tasks/", project_views.view_tasks, name="tasks"),
    path("<str:key>/calendar/", project_views.view_calendar, name="calendar"),
    path("<str:key>/inventory/", project_views.view_inventory, name="inventory"),
    path("<str:key>/wiki/", include("www.views.project.wiki.urls")),
    path("<str:key>/journal/", include("www.views.project.journal.urls")),
]
