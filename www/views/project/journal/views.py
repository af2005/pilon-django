from django.http import HttpResponse

from www.models import JournalPage, Project
from www.views import templates
import www.views.project.views as project_views
from ..views import ProjectContext
from django.views.generic import DetailView, ListView, CreateView


class JournalBase(ProjectContext):
    model = JournalPage
    fields = ["parent", "name", "markdown"]


class JournalHomepage(JournalBase, ListView):
    template_name = "www/project/journal/journal_page_list.html"


class JournalDetail(JournalBase, DetailView):
    template_name = "www/project/journal/journal_page_detail.html"


class JournalCreate(JournalBase, CreateView):
    template_name = "www/project/journal/journal_page_create.html"


class JournalPageCreateFromFile(JournalBase, CreateView):
    template_name = "www/project/journal/journal_page_create_from_file.html"