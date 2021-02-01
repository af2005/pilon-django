from django.urls import path, include

from . import project, people, admin, login, content, dashboard
from django.contrib.auth import views as auth_views

from .admin import main

urlpatterns = [
    path('accounts/login/',
         auth_views.LoginView.as_view(
             template_name="www/accounts/login.html"),
         #redirect_authenticated_user=True,
         ),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(
             template_name="www/accounts/logout.html"),
         #redirect_authenticated_user=True,
         ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', dashboard.view_dashboard, name='Dashboard'),
    path('login', login.view_login, name="Login"),
    path('logout', login.view_logout, name="Logout"),
    path('project/<str:key>', project.view_homepage, name="Project Homepage"),
    path('project-directory', project.view_directory, name="Project Directory"),
    path('create-project', project.view_create, name="Create Project"),
    path('people', people.directory, name="View People"),

    path('system-settings/<str:setting>', admin.main.system_settings, name="System settings")

]
