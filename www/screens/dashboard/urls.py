from . import main
from django.urls import path, include

urlpatterns = [
    path('', main.view_dashboard, name="View Dashboard"),
    path('dashboard/all-updates', main.view_all_updates_board, name="All updates board"),
    path('dashboard/last-worked-on', main.view_recently_worked_on_board, name="Last worked on board"),
]