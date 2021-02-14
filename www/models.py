import uuid

from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from polymorphic_tree.models import PolymorphicMPTTModel, PolymorphicTreeForeignKey

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

import reversion


@reversion.register()
class Entity(PolymorphicMPTTModel):
    #: Whether the node type allows to have children.
    can_have_children = True

    #: Whether the node type can be a root node.
    can_be_root = True

    #: Allowed child types for this page.
    child_types = []

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
        verbose_name = _("Entity")
        verbose_name_plural = _("Entities")


@reversion.register()
class Project(Entity):
    key = models.CharField(
        max_length=20,
        unique=True,
        primary_key=True,
    )

    class Meta(PolymorphicMPTTModel.Meta):
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")


@reversion.register()
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


@reversion.register()
class WikiPage(MarkdownEntity):
    class Meta(PolymorphicMPTTModel.Meta):
        verbose_name = _("Wiki Page")
        verbose_name_plural = _("Wiki Pages")


@reversion.register()
class JournalPage(MarkdownEntity):
    date = models.DateTimeField(default=timezone.now)


@reversion.register()
class Task(MarkdownEntity):
    due_date = models.DateTimeField(null=True)
    assignee = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="Assignee"
    )
    content = models.TextField()


@reversion.register()
class Comment(MarkdownEntity):
    pass


@reversion.register()
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
