from django.urls import path
from .views import JournalPageCreate, JournalHome, JournalPageDetail

urlpatterns = [
    path("", JournalHome.as_view(), name="journal"),
    path("create/", JournalPageCreate.as_view(), name="journal-page-create"),
    path(
        "create-from-file/",
        JournalPageCreate.as_view(),
        name="journal-page-create-from-file",
    ),
    path(
        "view/<slug:id>", JournalPageDetail.as_view(), name="journal-page-detail"
    ),  # this must be the last url
]
