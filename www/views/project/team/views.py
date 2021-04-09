from django.views.generic import TemplateView
from ..views import ProjectContext


class TeamView(ProjectContext, TemplateView):
    template_name = "www/project/team/team_detail.html"
    title_ = "Team"
    extra_context = {
        "page_title": title_,
        "window_title": title_,
        "active_sidebar_item": title_
    }
