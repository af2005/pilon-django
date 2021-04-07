from django.urls import path
from .views import ChatDetail

urlpatterns = [
    path("", ChatDetail.as_view(), name="chat"),
]
