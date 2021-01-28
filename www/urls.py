from django.urls import path

from . import views
from .screens import project, people

urlpatterns = [
    path('', views.view_dashboard, name='Dashboard'),
    path('login/', views.login, name="Login"),
    path('project/<str:key>', project.view_homepage, name="Project Homepage"),
    path('project-directory', project.view_directory, name="Project Directory"),
    path('create-project', project.view_create, name="Create Project"),
    path('people', people.directory, name="View People"),
]