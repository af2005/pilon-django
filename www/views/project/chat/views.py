from django.views.generic import DetailView
from ..views import ProjectContext


class ChatBase(ProjectContext):
    pass


class ChatDetail(ChatBase, DetailView):
    template_name = "www/project/chat/chat_detail.html"
