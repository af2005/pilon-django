from django.urls import path

from . import project, users

urlpatterns = [
    path('project', project.rest_handler_all, name="Project Info"),
    path('users', users.list_all_users, name="List all users")
]
