from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.view_content_create, name="create-wiki-page"),
    path(
        "create-from-file/", views.view_content_create, name="create-wiki-page-from-file"
    ),
    path("", views.view_wiki_homepage, name="wiki"),
]
