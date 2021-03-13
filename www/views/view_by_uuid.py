from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect


import www.views.project.wiki.views as wiki
import www.views.project.journal.views as journal
import www.views.project.tasks.views as task

from www.models import Entity, Project, WikiPage, JournalPage, Task


def main(request, uuid):
    entity = Entity.objects.filter(id=uuid).first()
    try:
        if isinstance(entity, WikiPage):
            project = entity.get_ancestors_of_type(Project).first()
            return wiki.view_wiki_page(request, key=project.key, uuid=uuid)

        if isinstance(entity, JournalPage):
            project = entity.get_ancestors_of_type(Project).first()
            return journal.view_journal(request, key=project.key)

        if isinstance(entity, Task):
            project = entity.get_ancestors_of_type(Project).first()
            return task.view_tasks(request, key=project.key)

        if isinstance(entity, Project):
            return redirect(reverse("project:homepage", args=[entity.key]))

    except AttributeError:
        if isinstance(entity, Project):
            pass
        # orphaned page
        # TODO

        pass

    return HttpResponseNotFound()
