from django.urls import path, include
from . import views

app_name = "project"

urlpatterns = [
    path("<str:key>/", views.homepage, name="homepage"),
    path("<str:key>/create/", views.content_create, name="create-child-entity"),
    path("<str:key>/team/", views.team, name="team"),
    path("<str:key>/chat/", views.chat, name="chat"),
    path("<str:key>/tasks/", include("www.views.project.tasks.urls"), name="tasks"),
    path("<str:key>/calendar/", views.calendar, name="calendar"),
    path("<str:key>/inventory/", views.inventory, name="inventory"),
    path("<str:key>/wiki/", include("www.views.project.wiki.urls")),
    path("<str:key>/journal/", include("www.views.project.journal.urls")),
]
