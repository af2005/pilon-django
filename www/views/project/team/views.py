from django.views.generic import TemplateView
from ..views import ProjectContext


class TeamView(ProjectContext, TemplateView):
    template_name = "www/project/team/team_detail.html"
