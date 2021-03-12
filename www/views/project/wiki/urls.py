from django.urls import path
from . import wiki_views

urlpatterns = [
    path("create/", wiki_views.view_content_create, name="create-wiki-page"),
    path(
        "create-from-file/", wiki_views.view_content_create, name="create-wiki-page-from-file"
    ),
    path("", wiki_views.view_wiki_homepage, name="wiki"),
]
