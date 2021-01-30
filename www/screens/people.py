from django.http import HttpResponse
from django.template import loader


def directory(request):
    template = loader.get_template('www/default.html')
    context = {
        'window_title': "People",
        'page_title': "People directory",
        'sidebar': False

    }
    return HttpResponse(template.render(context, request))
