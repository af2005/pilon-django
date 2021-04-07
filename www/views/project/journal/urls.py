from django.urls import path
from .views import JournalPageCreate, JournalHomepage, JournalPageDetail

urlpatterns = [
    path("", JournalHomepage.as_view(), name="journal"),
    path("create/", JournalPageCreate.as_view(), name="journal-page-create"),
    path(
        "create-from-file/",
        JournalPageCreate.as_view(),
        name="journal-page-create-from-file",
    ),
    path(
        "view/<slug:pk>", JournalPageDetail.as_view(), name="journal-page-detail"
    ),  # this must be the last url
]
