from django.urls import path, include
from . import project_views

urlpatterns = [
    path("", include("www.views.project.contents.urls")),

]
