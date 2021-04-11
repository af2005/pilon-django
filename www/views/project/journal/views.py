from www.models.entity import JournalPage
from ..views import ProjectContext
from django.views.generic import DetailView, ListView, CreateView


class JournalBase(ProjectContext):
    model = JournalPage
    fields = ["parent", "name", "markdown"]
    active_sidebar_item = "Journal"


class JournalHome(JournalBase, ListView):
    template_name = "www/project/journal/journal_page_list.html"


class JournalPageDetail(JournalBase, DetailView):
    template_name = "www/project/journal/journal_page_detail.html"


class JournalPageCreate(JournalBase, CreateView):
    template_name = "www/project/journal/journal_page_create.html"


class JournalPageCreateFromFile(JournalBase, CreateView):
    template_name = "www/project/journal/journal_page_create_from_file.html"
