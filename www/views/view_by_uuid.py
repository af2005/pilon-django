from django.http import HttpResponseNotFound
from django.urls import reverse
from django.shortcuts import redirect


import www.views.project.wiki.views
import www.views.project.journal.views
import www.views.project.tasks.views

from www.models.models import Entity, Project, WikiPage, JournalPage, Task


def main(request, uuid):
    entity = Entity.objects.filter(id=uuid).first()
    # return "Not Implemented"
    try:
        if isinstance(entity, WikiPage):
            project = entity.get_ancestors_of_type(Project).first()
            return www.views.project.wiki.views.WikiPageDetail(request, key=project.key, uuid=uuid)

        if isinstance(entity, JournalPage):
            project = entity.get_ancestors_of_type(Project).first()
            return www.views.project.journal.views.JournalPageDetail(
                request, key=project.key, uuid=uuid
            )

        if isinstance(entity, Task):
            project = entity.get_ancestors_of_type(Project).first()
            return www.views.project.tasks.views.TaskHome(request, key=project.key)

        if isinstance(entity, Project):
            return redirect(reverse("project:home", args=[entity.key]))

    except AttributeError:
        if isinstance(entity, Project):
            pass
        # orphaned page
        # TODO

        pass

    return HttpResponseNotFound()
