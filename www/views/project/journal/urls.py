from django.urls import path
from . import views

urlpatterns = [
    path("create", views.JournalCreate.as_view(), name="create-journal-page"),
    path(
        "create-from-file",
        views.JournalCreate.as_view(),
        name="create-journal-page-from-file",
    ),
    path("", views.homepage, name="journal"),
]
