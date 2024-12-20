from www.models.entity import JournalPage
from ..views import ProjectContext
from django.views.generic import DetailView, ListView, CreateView, UpdateView


class JournalBase(ProjectContext):
    model = JournalPage
    fields = ["parent", "name", "markdown"]
    active_sidebar_item = "Journal"
    extra_context = {"page_title": ""}


class JournalHome(JournalBase, ListView):
    paginate_by = 10
    template_name = "www/project/journal/journal_page_list.html"
    extra_context = {"page_title": "Last updated"}


class JournalPageDetail(JournalBase, DetailView):
    template_name = "www/project/journal/journal_page_detail.html"


class JournalPageCreate(JournalBase, CreateView):
    template_name = "www/project/journal/journal_page_create.html"


class JournalPageEdit(JournalBase, UpdateView):
    template_name = "www/project/journal/journal_page_edit.html"


class JournalPageCreateFromFile(JournalBase, CreateView):
    template_name = "www/project/journal/journal_page_create_from_file.html"
