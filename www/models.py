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
    can_be_root = False

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
        User,
        on_delete=models.SET_NULL,
        related_name="EntityCreator",
        null=True,
        default=None,
        blank=True,
    )

    class Meta(PolymorphicMPTTModel.Meta):
        verbose_name = _("Entity")
        verbose_name_plural = _("Entities")

    def repr(self):
        return {"id": self.id}


@reversion.register(follow=["entity_ptr"])
class Project(Entity):
    can_be_root = True

    key = models.CharField(max_length=20, unique=True)

    class Meta(PolymorphicMPTTModel.Meta):
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")


@reversion.register(follow=["entity_ptr"])
class MarkdownEntity(Entity):
    markdown = MarkdownField(
        default="",
        rendered_field="content_rendered",
        validator=VALIDATOR_STANDARD,
        use_editor=False,
        use_admin_editor=True,
        blank=True,
    )
    markdown_rendered = RenderedMarkdownField(default="")


@reversion.register(follow=["markdownentity_ptr"])
class WikiPage(MarkdownEntity):
    can_be_root = True

    class Meta(PolymorphicMPTTModel.Meta):
        verbose_name = _("Wiki Page")
        verbose_name_plural = _("Wiki Pages")


@reversion.register(follow=["markdownentity_ptr"])
class JournalPage(MarkdownEntity):
    child_types = ["Task", "Comment", "Attachment"]

    date = models.DateTimeField(default=timezone.now)


@reversion.register(follow=["markdownentity_ptr"])
class Task(MarkdownEntity):
    can_have_children = True
    child_types = ["Task", "Comment", "Attachment"]

    due_date = models.DateTimeField(null=True)
    assignee = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name="Assignee"
    )
    content = models.TextField()


@reversion.register(follow=["markdownentity_ptr"])
class Comment(MarkdownEntity):
    can_have_children = True
    child_types = ["Comment", "Attachment"]


@reversion.register(follow=["entity_ptr"])
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
