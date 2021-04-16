from django.urls import path, re_path
from .views import (
    WikiHome,
    WikiPageCreate,
    WikiPageCreateFromFile,
    WikiPageDetail,
    WikiPageEdit,
)

urlpatterns = [
    path("", WikiHome.as_view(), name="wiki"),
    path("create/", WikiPageCreate.as_view(), name="wiki-page-create"),
    path("edit/<slug:id>/", WikiPageEdit.as_view(), name="wiki-page-edit"),
    path("create-from-file/", WikiPageCreateFromFile.as_view(), name="wiki-page-create-from-file"),
    # this must be the last url
    path("view/<slug:id>", WikiPageDetail.as_view(), name="wiki-page-detail"),
]
