from . import views
from django.urls import path

urlpatterns = [
    path(
        "<str:setting>/",
        views.system_settings,
        name="System settings",
    ),
]
