from django.http import HttpResponse
from django.template import loader
from . import templates


def directory(request):
    tpl = templates.default(request, window_title="People", title="People directory", sidebar=False)
    return HttpResponse(tpl)
