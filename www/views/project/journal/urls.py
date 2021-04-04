from django.urls import path
from . import views

urlpatterns = [
    path("", views.JournalHomepage.as_view(), name="journal"),
    path("create/", views.JournalPageCreate.as_view(), name="journal-page-create"),
    path(
        "create-from-file/",
        views.JournalPageCreate.as_view(),
        name="journal-page-create-from-file",
    ),
    path(
        "view/<slug:pk>", views.JournalPageDetail.as_view(), name="journal-page-detail"
    ),  # this must be the last url
]
