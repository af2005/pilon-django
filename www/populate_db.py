from django.db import transaction
from django.core.management import call_command
from www.models import Project, WikiPage, JournalPage, Comment, User, Group, Entity


def populate_db(apps, schema_editor):
    with transaction.atomic():
        test_group = Group(name="TestGroup")
        test_group.save()
        test_user = User(
            username="TestUser",
            first_name="Hans",
            last_name="Wurst",
        )
        test_user.set_password(raw_password="password")
        test_user.save()
        test_user.groups.add(test_group)
        admin_user = User(username="admin", is_superuser=True, is_staff=True)
        admin_user.set_password(raw_password="password")
        admin_user.save()

        test_project = Project(name="Test Project", key="test", creator=test_user)
        test_project.save()
        WikiPage(name="Test Wiki Page", creator=test_user, parent=test_project).save()
        journal = JournalPage(name="Test Journal Page", parent=test_project)
        journal.save()
        WikiPage(name="Orphaned Page", creator=test_user).save()
        Comment(name="First Comment", parent=journal).save()

        call_command("createinitialrevisions")


def depopulate_db():
    Entity.objects.all().delete()
