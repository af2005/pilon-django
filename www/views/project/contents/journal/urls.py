from django.urls import path, include
from . import journal_views

urlpatterns = [
    path("create", journal_views.view_content_create, name="Create Journal Page"),
    path(
        "create-with-file/",
        journal_views.view_content_create,
        name="Create Journal Page with file",
    ),
    path("", journal_views.view_journal, name="Project Journal"),
]
