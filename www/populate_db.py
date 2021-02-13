from django.db import transaction
from www.models import Project, WikiPage, JournalPage, Comment, User, Group, Entity


def populate_db(apps, schema_editor):
    with transaction.atomic():
        test_group = Group(name="TestGroup")
        test_group.save()
        test_user = User(
            username="TestUser",
            password="password",
            first_name="Hans",
            last_name="Wurst",
        )
        test_user.save()
        test_user.groups.add(test_group)

        test_project = Project(name="Test Project", key="TEST", creator=test_user)
        test_project.save()
        WikiPage(name="Test Wiki Page", creator=test_user, parent=test_project).save()
        journal = JournalPage(name="Test Journal Page", parent=test_project)
        journal.save()
        WikiPage(name="Orphaned Page", creator=test_user).save()
        Comment(name="First Comment", parent=journal).save()


def depopulate_db():
    Entity.objects.all().delete()

