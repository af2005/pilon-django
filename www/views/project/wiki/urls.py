from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.WikiHomepage.as_view(), name="wiki"),
    path("create/", views.WikiPageCreate.as_view(), name="wiki-page-create"),
    path("update/<slug:pk>/", views.WikiPageUpdate.as_view(), name="wiki-page-update"),
    path("create-from-file/", views.content_create, name="create-wiki-page-from-file"),
    path(
        "<slug:pk>", views.WikiPageDetail.as_view(), name="wiki-page-detail"
    ),  # this must be the last url
]
