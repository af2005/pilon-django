import uuid

from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone

from polymorphic_tree.models import PolymorphicMPTTModel, PolymorphicTreeForeignKey

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD


class Entity(PolymorphicMPTTModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    parent = PolymorphicTreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="creator", null=True, default=None
    )

    class Meta(PolymorphicMPTTModel.Meta):
        verbose_name = "Tree node"
        verbose_name_plural = "Tree nodes"


class Project(Entity):
    key = models.CharField(max_length=20, primary_key=True)


class MarkdownEntity(Entity):
    markdown = MarkdownField(
        default="",
        rendered_field="content_rendered",
        validator=VALIDATOR_STANDARD,
        use_editor=False,
        use_admin_editor=True,
    )
    markdown_rendered = RenderedMarkdownField(default="")

    def repr(self):
        return {"id": self.id}


class WikiPage(MarkdownEntity):
    pass


class JournalPage(MarkdownEntity):
    date = models.DateTimeField(default=timezone.now)


class Task(MarkdownEntity):
    due_date = models.DateTimeField(null=True)
    assignee = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="Assignee"
    )
    content = models.TextField()


class Comment(MarkdownEntity):
    pass


class Attachment(Entity):
    RENDERABLE_FILE_TYPES = (
        "png",
        "gif",
        "jpeg",
        "jpg",
        "pdf",
        "svg",
        # "eps",
        "html",
        "docx",
        "pptx",
        "bmp",
    )

    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=255)
    file_path = ""  # todo create uuid

    @property
    def renderable(self):
        return self.file_type in self.RENDERABLE_FILE_TYPES
