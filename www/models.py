import shortuuid

from django.db import models
import django.contrib.auth.models as auth_models
import inflection
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from shortuuidfield import ShortUUIDField
from polymorphic_tree.models import (
    PolymorphicMPTTModel,
    PolymorphicTreeForeignKey,
    _get_base_polymorphic_model,
)

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


class ShortUUIDPolymorphicTreeForeignKey(PolymorphicTreeForeignKey):
    def _validate_parent(self, parent, model_instance):
        base_model = _get_base_polymorphic_model(model_instance.__class__)
        parent = base_model.objects.get(pk=parent)
        super()._validate_parent(parent, model_instance)


@reversion.register()
class Entity(PolymorphicMPTTModel, RandomUUIDMixin, SluggedNameMixin):
    #: Whether the node type allows to have children.
    can_have_children = True

    #: Whether the node type can be a root node.
    can_be_root = False

    #: Allowed child types for this page.
    child_types = []

    parent = ShortUUIDPolymorphicTreeForeignKey(
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

    def get_absolute_url(self):
        project = self.get_ancestors_of_type(Project).first()
        return reverse(
            f"project:{inflection.dasherize(inflection.underscore(self.__class__.__name__))}-detail",
            kwargs={"key": project.key, "pk": self.id},
        )

    @property
    def comments(self):
        return self.get_descendants().instance_of(Comment)


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

    @property
    def wiki_page_tree(self):
        return self.get_descendants().instance_of(WikiPage)

    @property
    def sidebar_items(self):
        return [
            {
                "name": "Home",
                "url": reverse("project:home", args=[self.key]),
                "icon": "house-fill",
            },
            {
                "name": "Team",
                "url": reverse("project:team", args=[self.key]),
                "icon": "people",
            },
            {
                "name": "Chat",
                "url": reverse("project:chat", args=[self.key]),
                "icon": "envelope",
            },
            {
                "name": "Tasks",
                "url": reverse("project:tasks", args=[self.key]),
                "icon": "check2-circle",
            },
            {
                "name": "Calendar",
                "url": reverse("project:calendar", args=[self.key]),
                "icon": "calendar3",
            },
            {
                "name": "Inventory",
                "url": reverse("project:inventory", args=[self.key]),
                "icon": "archive",
            },
            {
                "name": "Wiki",
                "url": reverse("project:wiki", args=[self.key]),
                "icon": "file-text",
            },
            {
                "name": "Journal",
                "url": reverse("project:journal", args=[self.key]),
                "icon": "journals",
            },
        ]


@reversion.register(follow=["entity_ptr"])
class MarkdownEntity(Entity):
    markdown = MarkdownField(
        default="",
        rendered_field="markdown_rendered",
        validator=VALIDATOR_STANDARD,
        use_editor=False,
        use_admin_editor=False,
        blank=True,
    )
    markdown_rendered = RenderedMarkdownField(default="")


@reversion.register(follow=["markdownentity_ptr"])
class WikiPage(MarkdownEntity):
    can_be_root = False

    class Meta(PolymorphicMPTTModel.Meta):
        verbose_name = _("Wiki Page")
        verbose_name_plural = _("Wiki Pages")

    @property
    def breadcrumbs(self):
        return self.get_ancestors_of_type(WikiPage)


@reversion.register(follow=["markdownentity_ptr"])
class JournalPage(MarkdownEntity):
    child_types = ["Task", "Comment", "Attachment"]

    date = models.DateTimeField(default=timezone.now)


@reversion.register(follow=["markdownentity_ptr"])
class Task(MarkdownEntity):
    child_types = ["Task", "Comment", "Attachment"]

    due_date = models.DateTimeField(null=True, blank=True)
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
