from django.urls import path, include
from . import main

urlpatterns = [
    path('<str:key>', main.view_homepage, name="Project Homepage"),
    path('<str:key>/create', main.view_content_create, name="Content create"),
    path('<str:key>/create/', include('www.screens.project.contents.create.urls')),
    path('<str:key>/team', main.view_team, name="Project Tasks"),
    path('<str:key>/chat', main.view_chat, name="Project Chat"),
    path('<str:key>/tasks', main.view_tasks, name="Project Tasks"),
    path('<str:key>/calendar', main.view_calendar, name="Project Calendar"),
    path('<str:key>/inventory', main.view_inventory, name="Project Inventory"),
    path('<str:key>/wiki', main.view_wiki, name="Project Wiki"),
    path('<str:key>/journal', main.view_journal, name="Project Journal"),
]
