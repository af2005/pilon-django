from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.WikiHomepage.as_view(), name="wiki"),
    path("create/", views.WikiPageCreate.as_view(), name="wiki-page-create"),
    path("edit/<slug:pk>/", views.WikiPageEdit.as_view(), name="wiki-page-edit"),
    path(
        "create-from-file/",
        views.content_create_with_file,
        name="create-wiki-page-from-file",
    ),
    path(
        "view/<slug:pk>", views.WikiPageDetail.as_view(), name="wiki-page-detail"
    ),  # this must be the last url
]
