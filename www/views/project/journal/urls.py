from django.urls import path
from . import journal_views

urlpatterns = [
    path("create", journal_views.view_content_create, name="create-journal-page"),
    path(
        "create-from-file/",
        journal_views.view_content_create,
        name="create-journal-page-from-file",
    ),
    path("", journal_views.view_journal, name="journal"),
]
