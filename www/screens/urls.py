from django.urls import path, include

from . import project, people, admin, content, dashboard, user_settings
from django.contrib.auth import views as auth_views

from .admin import main

urlpatterns = [
    path('accounts/login/',
         auth_views.LoginView.as_view(
             template_name="www/accounts/login.html")
         ),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(
             template_name="www/accounts/logout.html"),
         ),
    path('accounts/settings/',user_settings.main, name="User settings"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', dashboard.view_dashboard, name='Dashboard'),
    path('project/contents/<str:key>', project.view_homepage, name="Project Homepage"),
    path('project/contents/<str:key>/team', project.view_team, name="Project Tasks"),
    path('project/contents/<str:key>/tasks', project.view_tasks, name="Project Tasks"),
    path('project/contents/<str:key>/calendar', project.view_calendar, name="Project Calendar"),
    path('project/contents/<str:key>/wiki', project.view_wiki, name="Project Wiki"),
    path('project/contents/<str:key>/journal', project.view_journal, name="Project Journal"),

    path('project/directory', project.view_directory, name="Project Directory"),
    path('project/create', project.view_project_create, name="Create Project"),
    path('people', people.directory, name="View People"),
    path('system-settings/<str:setting>', admin.main.system_settings, name="System settings"),
    path('dashboard/all-updates', dashboard.view_all_updates_board, name="All updates board"),
    path('dashboard/last-worked-on', dashboard.view_recently_worked_on_board, name="Last worked on board"),
]
