from django.template import loader


def get(request, window_title, title="", subtitle="", sidebar=False, sidebar_items=None, content=None):
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
