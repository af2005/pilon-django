from django.urls import path

from . import project

urlpatterns = [
    path('project', project.rest_handler_all, name="Project Info"),

]