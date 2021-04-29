from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("", include("www.views.urls")),
    path("rest/", include("www.rest.urls")),
    path("schedule/", include("schedule.urls")),

]
