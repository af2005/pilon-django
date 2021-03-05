from django.urls import path, include

from . import people, admin, user_settings, view_by_id, project_helper_views
from django.contrib.auth import views as auth_views
from django.views.defaults import page_not_found

from .admin import admin_views

urlpatterns = [
    path("", include("www.views.dashboard.urls")),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="www/accounts/login.html"),
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(template_name="www/accounts/logout.html"),
    ),
    path("accounts/settings/", user_settings.main, name="User settings"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("project/", include("www.views.project.urls")),
    path("project-directory/", project_helper_views.view_directory, name="Project Directory"),
    path("project-create/", project_helper_views.view_project_create, name="Create Project"),
    path("id/", page_not_found, name="Content by UID root"),
    path("id/<str:uid>", view_by_id.main, name="Content by UID"),
    path("people/", people.directory, name="View People"),
    path(
        "system-settings/<str:setting>/",
        admin.admin_views.system_settings,
        name="System settings",
    ),
]