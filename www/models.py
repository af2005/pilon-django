import shortuuid

from django.db import models
import django.contrib.auth.models as auth_models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from shortuuidfield import ShortUUIDField
from polymorphic_tree.models import PolymorphicMPTTModel, PolymorphicTreeForeignKey

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD
from colorfield.fields import ColorField

import reversion


class RandomUUIDMixin(models.Model):
    id = ShortUUIDField(primary_key=True, default=shortuuid.uuid)

    class Meta:
        abstract = True


class SluggedNameMixin(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class User(auth_models.AbstractUser, RandomUUIDMixin):
    pass


class Group(auth_models.Group, RandomUUIDMixin):
    pass


@reversion.register()
class Entity(PolymorphicMPTTModel, RandomUUIDMixin, SluggedNameMixin):
    #: Whether the node type allows to have children.
    can_have_children = True

    #: Whether the node type can be a root node.
    can_be_root = False

    #: Allowed child types for this page.
    child_types = []

    parent = PolymorphicTreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    date_modified = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="created_entities",
        null=True,
        default=None,
        blank=True,
    )

    class Meta(PolymorphicMPTTModel.Meta):
        verbose_name = _("Entity")
        verbose_name_plural = _("Entities")

    def repr(self):
        return {"id": self.id}


@reversion.register()
class Label(RandomUUIDMixin, SluggedNameMixin):
    name = models.CharField(unique=True, max_length=50)
    entities = models.ManyToManyField(Entity, related_name="labels")


@reversion.register(follow=["entity_ptr"])
class Project(Entity):
    can_be_root = True

    key = models.CharField(max_length=20, unique=True)
    color = ColorField(default="#FF0000", blank=True)

    class Meta(PolymorphicMPTTModel.Meta):
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")


@reversion.register(follow=["entity_ptr"])
class MarkdownEntity(Entity):
    markdown = MarkdownField(
        default="",
        rendered_field="markdown_rendered",
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
    child_types = ["Task", "Comment", "Attachment"]

    due_date = models.DateTimeField(null=True)
    assignee = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name="tasks"
    )


@reversion.register(follow=["markdownentity_ptr"])
class Comment(MarkdownEntity):
    child_types = ["Comment", "Attachment"]


@reversion.register(follow=["entity_ptr"])
class Attachment(Entity):
    can_have_children = False

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
