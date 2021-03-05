from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound

from www.models import Entity, Project, WikiPage, JournalPage


def main(request, uid):
    wiki_page = Entity.objects.filter(Q(instance_of=WikiPage), id=uid).first()
    try:
        if wiki_page:
            project = wiki_page.get_ancestors_of_type(Project).first()
            # Wiki Page View
            import www.screens.project.contents.wiki.main as wiki
            return wiki.view_wiki_page(request, key=project.key, uid=uid)

        journal_page = Entity.objects.filter(Q(instance_of=JournalPage), id=uid).first()
        if journal_page:
            project = journal_page.get_ancestors_of_type(Project).first()
            #TODO

    except AttributeError:
        # orphaned page
        # TODO
        pass

    return HttpResponseNotFound()
