from django.urls import path, include

from . import people, admin, user_settings
from django.contrib.auth import views as auth_views

from .admin import main

urlpatterns = [
    path('', include('www.screens.dashboard.urls')),
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

]
