from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskHome.as_view(), name="tasks"),
    path("create/", views.TaskCreate.as_view(), name="task-create"),
    path("edit/<slug:pk>/", views.TaskEdit.as_view(), name="task-edit"),
    path(
        "view/<slug:pk>", views.TaskDetail.as_view(), name="task-detail"
    ),  # this must be the last url
]
