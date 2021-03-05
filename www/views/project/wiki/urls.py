from django.urls import path
from . import wiki_views

urlpatterns = [
    path("create/", wiki_views.view_content_create, name="Create Wiki Page"),
    path(
        "create-with-file/", wiki_views.view_content_create, name="Create Wiki Page with file"
    ),
    path("", wiki_views.view_wiki_homepage, name="Project Wiki"),
]
