from django.template import loader


def admin(request, window_title, title="", subtitle="", sidebar_items=None, content=None):
    template = loader.get_template('www/admin.html')
    context = {
        'window_title': window_title,
        'page_title': title,
        'page_subtitle': subtitle,
        'sidebar_items': sidebar_items,
        'content': content
    }
    return template.render(context, request)


def simple(request, window_title, title="", subtitle="", content=""):
    template = loader.get_template('www/simple.html')
    context = {
        'window_title': window_title,
        'content': content,
        'page_title': title,
        'page_subtitle': subtitle,
    }
    return template.render(context, request)


def dashboard(request, window_title, title="", subtitle="", subnav_items=None, active_subnav_item=None, content=""):
    template = loader.get_template('www/dashboard/dashboard.html')
    context = {
        'window_title': window_title,
        'page_title': title,
        'page_subtitle': subtitle,
        'subnav_items': subnav_items,
        'active_subnav_item': active_subnav_item,
        'content': content
    }
    return template.render(context, request)


def people(request, window_title, title="", subtitle="", users=[]):
    template = loader.get_template('www/people.html')
    context = {
        'window_title': window_title,
        'page_title': title,
        'page_subtitle': subtitle,
        'users': users
    }
    return template.render(context, request)
