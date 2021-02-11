import uuid

from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from mptt.models import MPTTModel, TreeForeignKey

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD


class Entity(MPTTModel):
    ENTITY_TYPE = models.CharField(max_length=255, default="Entity")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )
    object_id = models.PositiveIntegerField(null=True)
    parent_object = GenericForeignKey(
        "content_type",
        "object_id",
    )
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="creator", null=True, default=None
    )

    class MPTTMeta:
        order_insertion_by = ["name"]


class Project(Entity):
    ENTITY_TYPE = "Project"

    key = models.CharField(
        max_length=20,
        unique=True,
        primary_key=True,
    )


class MarkdownEntity(Entity):
    ENTITY_TYPE = "MarkdownEntity"

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
    ENTITY_TYPE = "WikiPage"

    pass


class JournalPage(MarkdownEntity):
    ENTITY_TYPE = "JournalPage"
    date = models.DateTimeField(default=timezone.now)


class Task(MarkdownEntity):
    ENTITY_TYPE = "Task"

    due_date = models.DateTimeField(null=True)
    assignee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Assignee", null=True
    )
    content = models.TextField()


class Comment(MarkdownEntity):
    ENTITY_TYPE = "Comment"
    pass


class Attachment(Entity):
    ENTITY_TYPE = "Attachment"
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
