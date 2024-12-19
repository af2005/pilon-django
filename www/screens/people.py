from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from . import templates

@login_required
def directory(request):
    tpl = templates.default(request, window_title="People", title="People directory", sidebar=False)
    return HttpResponse(tpl)
