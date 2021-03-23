from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.content_create, name="create-wiki-page"),
    path("create-from-file/", views.content_create, name="create-wiki-page-from-file"),
    path("", views.wiki_homepage, name="wiki"),
]
