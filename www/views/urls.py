from django.urls import path, include

from . import people, admin, user_settings, view_by_uuid, project_helper_views
from django.contrib.auth import views as auth_views
from .project.views import ProjectList, ProjectCreate
from django.contrib.auth.decorators import user_passes_test
from .people import PeopleDirectory

urlpatterns = [
    path("", include("www.views.dashboard.urls")),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="www/accounts/login.html", redirect_authenticated_user=False
        ),
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(template_name="www/accounts/logout.html"),
    ),
    path("accounts/settings/", user_settings.main, name="user-settings"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("project/", include("www.views.project.urls")),
    path("project-directory/", ProjectList.as_view(), name="project-directory"),
    path("project-create/", ProjectCreate.as_view(), name="project-create"),
    path("id/<str:uuid>", view_by_uuid.main, name="Content by UUID"),
    path("people/", PeopleDirectory.as_view(), name="people-list"),
    path("system-settings/", include("www.views.admin.urls")),
]
