from django.contrib import admin
from polymorphic_tree.admin import (
    PolymorphicMPTTParentModelAdmin,
    PolymorphicMPTTChildModelAdmin,
)
from reversion_compare.admin import CompareVersionAdmin

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


class BaseChildAdmin(
    CompareVersionAdmin,
    PolymorphicMPTTChildModelAdmin,
):
    # object_history_template = "admin/polymorphic/object_history.html"
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


class EntityParentAdmin(CompareVersionAdmin, PolymorphicMPTTParentModelAdmin):
    # object_history_template = "admin/polymorphic/object_history.html"
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

    def compare_view(self, request, object_id, extra_context=None):
        """Redirect the reversion-compare view to the child admin."""
        real_admin = self._get_real_admin(object_id)
        return real_admin.compare_view(request, object_id, extra_context=extra_context)


admin.site.register(
    (Project, MarkdownEntity, WikiPage, JournalPage, Task, Comment, Attachment),
    BaseChildAdmin,
)
admin.site.register(Entity, EntityParentAdmin)
