from django.template import loader


def admin(request, window_title, title="", subtitle="", sidebar_items=None, content=None):
    template = loader.get_template("www/base/base+sidebar+title.html")
    context = {
        "window_title": window_title,
        "page_title": title,
        "page_subtitle": subtitle,
        "sidebar_items": sidebar_items,
        "content": content,
        "navbar_centertext": "System settings",
    }
    return template.render(context, request)
