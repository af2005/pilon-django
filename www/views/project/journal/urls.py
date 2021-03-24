from django.urls import path
from . import views

urlpatterns = [
    path("create", views.content_create, name="create-journal-page"),
    path(
        "create-from-file/",
        views.content_create,
        name="create-journal-page-from-file",
    ),
    path("", views.homepage, name="journal"),
]
