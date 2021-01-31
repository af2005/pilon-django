from django.template import loader


def default(request, window_title, title="", subtitle="", sidebar=False, sidebar_items=None, content=None):
    if sidebar_items is None:
        sidebar_items = []

    template = loader.get_template('www/default.html')
    context = {
        'window_title': window_title,
        'page_title': title,
        'page_subtitle': subtitle,
        'sidebar': sidebar,
        'sidebar_items': sidebar_items,
        'content': content
    }
    return template.render(context, request)


def admin(request, window_title, title="", subtitle="", sidebar=False, sidebar_items=None, content=None):
    template = loader.get_template('www/admin.html')
    context = {
        'window_title': window_title,
        'page_title': title,
        'page_subtitle': subtitle,
        'sidebar': sidebar,
        'sidebar_items': sidebar_items,
        'content': content
    }
    return template.render(context, request)


def project(request, window_title, title="", subtitle="", sidebar=False, sidebar_items=None, content=None):
    template = loader.get_template('www/project.html')
    context = {
        'window_title': window_title,
        'page_title': title,
        'page_subtitle': subtitle,
        'sidebar': sidebar,
        'sidebar_items': sidebar_items,
        'content': content
    }
    return template.render(context, request)
