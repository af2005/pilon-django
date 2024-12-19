from django.urls import path, include
from . import main

urlpatterns = [
    path('create', main.view_content_create, name="Create Journal Page"),
    path('', main.view_journal, name="Project Journal"),
]
