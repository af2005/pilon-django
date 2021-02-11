from django.urls import path, include
from . import main

urlpatterns = [
    path("create/", main.view_content_create, name="Create Wiki Page"),
    path("create-with-file/", main.view_content_create, name="Create Wiki Page with file"),
    path("", main.view_wiki, name="Project Wiki"),
]
