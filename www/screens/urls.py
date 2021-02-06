from django.urls import path, include

from . import project, people, admin, content, dashboard, user_settings
from django.contrib.auth import views as auth_views

from .admin import main

urlpatterns = [
    path('', dashboard.view_dashboard, name='Dashboard'),
    path('accounts/login/',
         auth_views.LoginView.as_view(
             template_name="www/accounts/login.html")
         ),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(
             template_name="www/accounts/logout.html"),
         ),
    path('accounts/settings/', user_settings.main, name="User settings"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('p/', include('www.screens.project.urls')),
    path('people', people.directory, name="View People"),
    path('system-settings/<str:setting>', admin.main.system_settings, name="System settings"),
    path('dashboard/all-updates', dashboard.view_all_updates_board, name="All updates board"),
    path('dashboard/last-worked-on', dashboard.view_recently_worked_on_board, name="Last worked on board"),
]
