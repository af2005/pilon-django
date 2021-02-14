from django.contrib import admin
from polymorphic_tree.admin import (
    PolymorphicMPTTParentModelAdmin,
    PolymorphicMPTTChildModelAdmin,
)
from reversion.admin import VersionAdmin
from .models import (
    Entity,
    Project,
    MarkdownEntity,
    WikiPage,
    JournalPage,
    Task,
    Comment,
    Attachment,
)


# The common admin functionality for all derived models:


class BaseChildAdmin(PolymorphicMPTTChildModelAdmin, VersionAdmin):
    object_history_template = "admin/polymorphic/object_history.html"
    GENERAL_FIELDSET = (
        None,
        {
            "fields": (
                "parent",
                "name",
            ),
        },
    )

    base_model = Entity
    base_fieldsets = (GENERAL_FIELDSET,)


# Optionally some custom admin code


class MarkdownEntityAdmin(BaseChildAdmin):
    pass


# Create the parent admin that combines it all:


class EntityParentAdmin(VersionAdmin, PolymorphicMPTTParentModelAdmin):
    object_history_template = "admin/polymorphic/object_history.html"
    base_model = Entity
    child_models = (
        Project,
        MarkdownEntity,
        WikiPage,
        JournalPage,
        Task,
        Comment,
        Attachment,
    )

    # list_display = ("name",)

    class Media:
        css = {"all": ("admin/treenode/admin.css",)}


admin.site.register(
    (Project, MarkdownEntity, WikiPage, JournalPage, Task, Comment, Attachment),
    BaseChildAdmin,
)
admin.site.register(Entity, EntityParentAdmin)
