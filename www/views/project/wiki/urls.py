from django.urls import path, re_path
from .views import (
    WikiHomepage,
    WikiPageCreate,
    WikiPageCreateFromFile,
    WikiPageDetail,
    WikiPageEdit,
)

urlpatterns = [
    path("", WikiHomepage.as_view(), name="wiki"),
    path("create/", WikiPageCreate.as_view(), name="wiki-page-create"),
    path("edit/<slug:pk>/", WikiPageEdit.as_view(), name="wiki-page-edit"),
    path("create-from-file/", WikiPageCreateFromFile.as_view(), name="create-wiki-page-from-file"),
    path(
        "view/<slug:pk>", WikiPageDetail.as_view(), name="wiki-page-detail"
    ),  # this must be the last url
]
