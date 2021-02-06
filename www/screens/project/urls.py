from django.urls import path, include
from . import main

urlpatterns = [
    path('c/', include('www.screens.project.contents.urls')),
    path('directory', main.view_directory, name="Project Directory"),
    path('create', main.view_project_create, name="Create Project")
]
