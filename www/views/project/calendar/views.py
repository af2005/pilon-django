from django.views.generic import TemplateView
from ..views import ProjectContext


class CalendarBase(ProjectContext):
    extra_context = {
        "window_title": "Calendar"
    }


class CalendarHome(CalendarBase, TemplateView):
    template_name = "www/project/calendar/calendar_home.html"
