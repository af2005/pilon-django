from django.urls import path
from . import views

urlpatterns = [
    path("create", views.view_content_create, name="create-journal-page"),
    path(
        "create-from-file/",
        views.view_content_create,
        name="create-journal-page-from-file",
    ),
    path("", views.view_journal, name="journal"),
]
