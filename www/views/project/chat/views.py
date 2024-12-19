from django.views.generic import TemplateView
from ..views import ProjectContext


class ChatBase(ProjectContext):
    active_sidebar_item = "Chat"


class ChatDetail(ChatBase, TemplateView):
    template_name = "www/project/chat/chat_detail.html"
