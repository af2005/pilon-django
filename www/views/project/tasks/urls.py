from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskHome.as_view(), name="tasks"),
    path("create/", views.TaskCreate.as_view(), name="task-create"),
    path("edit/<slug:id>/", views.TaskEdit.as_view(), name="task-edit"),
    path(
        "view/<slug:id>", views.TaskDetail.as_view(), name="task-detail"
    ),  # this must be the last url
]
