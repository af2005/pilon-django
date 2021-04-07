from django.urls import path, include
from . import views

app_name = "project"

urlpatterns = [
    path("<str:key>/", views.ProjectHomepage.as_view(), name="homepage"),
    path("<str:key>/create/", views.ContentCreate.as_view(), name="child-entity-create"),
    path("<str:key>/team/", include("www.views.project.team.urls"), name="team"),
    path("<str:key>/chat/", include("www.views.project.chat.urls"), name="chat"),
    path("<str:key>/tasks/", include("www.views.project.tasks.urls"), name="tasks"),
    path("<str:key>/calendar/", include("www.views.project.calendar.urls"), name="calendar"),
    path("<str:key>/inventory/", include("www.views.project.inventory.urls"), name="inventory"),
    path("<str:key>/wiki/", include("www.views.project.wiki.urls")),
    path("<str:key>/journal/", include("www.views.project.journal.urls")),
]
