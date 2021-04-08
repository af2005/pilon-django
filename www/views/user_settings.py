from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import templates
from django.views.generic import TemplateView


class UserSettingsHome(TemplateView):
    template_name = "www/user_settings_home.html"
    title_ = "User Settings"
    extra_context = {
        "window_title": title_,
        "page_title": title_,
        "navbar_centertext": title_}
