from django.urls import path, include
from . import views
app_name="project"

urlpatterns = [
    path("<str:key>/", views.view_homepage, name="homepage"),
    path("<str:key>/create/", views.view_content_create, name="create-child-entity"),
    path("<str:key>/team/", views.view_team, name="team"),
    path("<str:key>/chat/", views.view_chat, name="chat"),
    path("<str:key>/tasks/", include("www.views.project.tasks.urls"), name="tasks"),
    path("<str:key>/calendar/", views.view_calendar, name="calendar"),
    path("<str:key>/inventory/", views.view_inventory, name="inventory"),
    path("<str:key>/wiki/", include("www.views.project.wiki.urls")),
    path("<str:key>/journal/", include("www.views.project.journal.urls")),
]
