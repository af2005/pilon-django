from django.urls import path

from .screens import project, people, settings, login, content

urlpatterns = [
    path('', content.view_dashboard, name='Dashboard'),
    path('login', login.view_login, name="Login"),
    path('logout', login.view_logout, name="Logout"),
    path('project/<str:key>', project.view_homepage, name="Project Homepage"),
    path('project-directory', project.view_directory, name="Project Directory"),
    path('create-project', project.view_create, name="Create Project"),
    path('people', people.directory, name="View People"),
]