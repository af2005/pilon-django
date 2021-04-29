from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("", include("www.views.urls")),
    path("rest/", include("www.rest.urls")),
    path("schedule/", include("schedule.urls")),
    path('hello-webpack/', TemplateView.as_view(template_name='hello_webpack.html'))

]
