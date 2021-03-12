from django.urls import path, include

urlpatterns = [
    path("", include("www.views.urls")),
    path("rest/", include("www.rest.urls", namespace="rest")),
    path("schedule/", include("schedule.urls")),
]
