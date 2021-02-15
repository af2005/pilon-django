from django.db import transaction
from django.core.management import call_command
from www.models import Project, WikiPage, JournalPage, Comment, User, Group, Entity
from schedule.models import Calendar, Event, Rule
import datetime


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

        # Calendar
        try:
            cal = Calendar.objects.get(name="Example Calendar")
            print("It looks like you already have loaded this sample data, quitting.")
            import sys
            sys.exit(1)
        except Calendar.DoesNotExist:
            cal = Calendar(name="Example Calendar", slug="example")
            cal.save()
            rule = Rule(frequency="YEARLY", name="Yearly", description="will recur once every Year")
            rule.save()
            rule = Rule(frequency="MONTHLY", name="Monthly", description="will recur once every Month")
            rule.save()
            rule = Rule(frequency="WEEKLY", name="Weekly", description="will recur once every Week")
            rule.save()
            rule = Rule(frequency="DAILY", name="Daily", description="will recur once every Day")
            rule.save()

            today = datetime.date.today()
            rule = Rule.objects.get(frequency="WEEKLY")
            data = {
                'title': 'Exercise',
                'start': datetime.datetime(today.year, today.month, today.day, 9, 0),
                'end': datetime.datetime(today.year, today.month, today.day, 10, 0),
                'end_recurring_period': datetime.datetime(today.year + 1, 6, 1, 0, 0),
                'rule': rule,
                'calendar': cal
            }
            event = Event(**data)
            event.save()

    call_command("createinitialrevisions")


def depopulate_db():
    Entity.objects.all().delete()
