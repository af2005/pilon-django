from django.urls import path, include
from . import main, editor

urlpatterns = [
    path('c/<str:key>', main.view_homepage, name="Project Homepage"),
    path('c/<str:key>/create', main.view_content_create, name="Content create"),
    path('c/<str:key>/create/default-editor', editor.view_default_editor,
         name="Content create with default editor"),
    path('c/<str:key>/create/markdown-editor', editor.view_markdown_editor,
         name="Content create with markdown editor"),
    path('c/<str:key>/create/file-upload', editor.view_file_upload, name="Content create with file upload"),
    path('c/<str:key>/team', main.view_team, name="Project Tasks"),
    path('c/<str:key>/chat', main.view_chat, name="Project Chat"),
    path('c/<str:key>/tasks', main.view_tasks, name="Project Tasks"),
    path('c/<str:key>/calendar', main.view_calendar, name="Project Calendar"),
    path('c/<str:key>/inventory', main.view_inventory, name="Project Inventory"),
    path('c/<str:key>/wiki', main.view_wiki, name="Project Wiki"),
    path('c/<str:key>/journal', main.view_journal, name="Project Journal"),
    path('directory', main.view_directory, name="Project Directory"),
    path('create', main.view_project_create, name="Create Project")

]
