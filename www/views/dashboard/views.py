from django.views.generic import TemplateView
from django.urls import reverse_lazy

SUBNAV_ITEMS = [
    {"name": "Dashboard", "url": reverse_lazy("dashboard-view")},
    {"name": "All Updates", "url": reverse_lazy("dashboard-all-updates")},
    {"name": "Last Worked On", "url": reverse_lazy("dashboard-last-worked-on")},
]


class DashboardView(TemplateView):
    template_name = "www/dashboard/dashboard.html"
    extra_context = {
        "window_title": "Dashboard",
        "title": "Today",
        "subnav_items": SUBNAV_ITEMS,
        "active_subnav_item": 0
    }


class DashboardAllUpdates(TemplateView):
    template_name = "www/dashboard/dashboard_all_updates.html"
    extra_context = {
        "window_title": "All Updates",
        "title": "All Updates",
        "subnav_items": SUBNAV_ITEMS,
        "active_subnav_item": 1
    }


class DashboardLastWorkedOn(TemplateView):
    template_name = "www/dashboard/dashboard_last_worked_on.html"
    extra_context = {
        "window_title": "Recently Worked On",
        "title": "Recently Worked On",
        "subnav_items": SUBNAV_ITEMS,
        "active_subnav_item": 2
    }