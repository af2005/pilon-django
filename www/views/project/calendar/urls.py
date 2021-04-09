from django.urls import path
from .views import CalendarHome

urlpatterns = [
    path("", CalendarHome.as_view(), name="calendar"),
]
