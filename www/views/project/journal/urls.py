from django.urls import path
from .views import JournalCreate, JournalHomepage, JournalDetail

urlpatterns = [
    path("", JournalHomepage.as_view(), name="journal"),
    path("create/", JournalCreate.as_view(), name="journal-page-create"),
    path(
        "create-from-file/",
        JournalCreate.as_view(),
        name="journal-page-create-from-file",
    ),
    path(
        "view/<slug:pk>", JournalDetail.as_view(), name="journal-page-detail"
    ),  # this must be the last url
]
