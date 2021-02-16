from django.urls import path, include
from . import project, users


urlpatterns = [
    path("project", project.rest_handler_all, name="Project API"),
    path("users", users.list_all_users, name="List all users"),
]
