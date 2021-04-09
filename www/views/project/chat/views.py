from django.views.generic import TemplateView
from ..views import ProjectContext


class ChatBase(ProjectContext):
    title_ = "Chat"
    extra_context = {
        "window_title": title_,
        "active_sidebar_item": title_,
        "page_title": title_
    }


class ChatDetail(ChatBase, TemplateView):
    template_name = "www/project/chat/chat_detail.html"
