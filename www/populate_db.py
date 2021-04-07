from django.db import transaction
from django.core.management import call_command
from www.models import Project, WikiPage, JournalPage, Comment, User, Group, Entity
from schedule.models import Calendar, Event, Rule
import datetime
from lorem_text import lorem


def populate_db(apps, schema_editor):
    with transaction.atomic():
        test_user = populate_user_groups()
        populate_entities(test_user=test_user)
        populate_calendar()

    call_command("createinitialrevisions")


def depopulate_db():
    Entity.objects.all().delete()


def populate_calendar():
    # Calendar
    cal = Calendar(name="Test", slug="test")
    cal.save()
    cal = Calendar.objects.get(slug="test")
    rule = Rule(frequency="YEARLY", name="Yearly", description="will recur once every Year")
    rule.save()
    rule = Rule(
        frequency="MONTHLY",
        name="Monthly",
        description="will recur once every Month",
    )
    rule.save()
    rule = Rule(frequency="WEEKLY", name="Weekly", description="will recur once every Week")
    rule.save()
    rule = Rule(frequency="DAILY", name="Daily", description="will recur once every Day")
    rule.save()

    today = datetime.date.today()
    rule = Rule.objects.get(frequency="WEEKLY")
    data = {
        "title": "Exercise",
        "start": datetime.datetime(today.year, today.month, today.day, 9, 0),
        "end": datetime.datetime(today.year, today.month, today.day, 10, 0),
        "end_recurring_period": datetime.datetime(today.year + 1, 6, 1, 0, 0),
        "rule": rule,
        "calendar": cal,
    }
    event = Event(**data)
    event.save()


def populate_user_groups():
    test_group = Group(name="TestGroup")
    test_group.save()
    test_user = User(username="TestUser", first_name="Hans", last_name="Wurst")
    test_user.set_password(raw_password="password")
    test_user.save()
    test_user.groups.add(test_group)
    admin_user = User(username="admin", is_superuser=True, is_staff=True)
    admin_user.set_password(raw_password="password")
    admin_user.save()

    return test_user


def populate_entities(test_user):
    test_project = Project(name="Test Project", key="test", creator=test_user)
    test_project.save()
    populate_wiki(test_user, test_project)
    populate_journal(test_user, test_project)


def populate_wiki(test_user, test_project):
    WikiPage(name="Orphaned Page", creator=test_user, markdown=lorem.paragraph()).save()
    parent_page = WikiPage(
        name="Test Wiki Page", creator=test_user, parent=test_project, markdown=lorem.paragraph()
    )
    parent_page.save()
    Comment(name="Wiki Comment", parent=parent_page, markdown=lorem.sentence()).save()
    WikiPage(
        name="Test Wiki Page Child",
        creator=test_user,
        parent=parent_page,
        markdown=lorem.paragraph(),
    ).save()
    WikiPage(
        name="Child 2", creator=test_user, parent=parent_page, markdown=lorem.paragraph()
    ).save()
    WikiPage(
        name="Child 3", creator=test_user, parent=parent_page, markdown=lorem.paragraph()
    ).save()


def populate_journal(test_user, test_project):
    journal = JournalPage(
        name="Test Journal Page", creator=test_user, parent=test_project, markdown=lorem.paragraph()
    )
    journal.save()
    JournalPage(
        name="Test Journal Page 2",
        creator=test_user,
        date=datetime.datetime.now() - datetime.timedelta(days=10),
        parent=test_project,
        markdown=lorem.paragraph(),
    ).save()
    Comment(name="First Comment", parent=journal, markdown=lorem.sentence()).save()
