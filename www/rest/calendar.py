from django.http import HttpResponse
from schedule.models import Calendar, Event, Rule


def test(request):
    return HttpResponse("gal")
