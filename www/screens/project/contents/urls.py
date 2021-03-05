from django.urls import path, include
from . import main

urlpatterns = [
    path("<str:key>/", main.view_homepage, name="Project Homepage"),
    path("<str:key>/create/", main.view_content_create, name="Create Content"),
    path("<str:key>/team/", main.view_team, name="Project Team"),
    path("<str:key>/chat/", main.view_chat, name="Project Chat"),
    path("<str:key>/tasks/", main.view_tasks, name="Project Tasks"),
    path("<str:key>/calendar/", main.view_calendar, name="Project Calendar"),
    path("<str:key>/inventory/", main.view_inventory, name="Project Inventory"),
    path("<str:key>/wiki/", include("www.screens.project.contents.wiki.urls")),
    path("<str:key>/journal/", include("www.screens.project.contents.journal.urls")),
]
