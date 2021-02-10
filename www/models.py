import uuid

from django.db import models
from django.contrib.auth.models import User

from mptt.models import MPTTModel, TreeForeignKey

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

from datetime import datetime


class Content(MPTTModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    date_created = models.DateTimeField(default=datetime.now)
    date_modified = models.DateTimeField(default=datetime.now)
    author = ""

    class MPTTMeta:
        order_insertion_by = ["title"]


class Child(Content):
    space_key = models.CharField(max_length=20)


class Project(models.Model):
    key = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)


class Page(models.Model):
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    # version = models.IntegerField(default=0)
    content = MarkdownField(
        default="",
        rendered_field="content_rendered",
        validator=VALIDATOR_STANDARD,
        use_editor=False,
        use_admin_editor=True,
    )
    content_rendered = RenderedMarkdownField(default="")

    def repr(self):
        return {"id": self.id}


class WikiPage(Page):
    pass


class JournalPage(Page):
    date = models.DateTimeField()


class Task(models.Model):
    created_date = models.DateTimeField()
    due_date = models.DateTimeField()
    reporter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Reporter"
    )
    assignee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Assignee"
    )
    content = models.TextField()
