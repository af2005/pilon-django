# Generated by Django 3.1.6 on 2021-02-13 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import markdownfield.models
import polymorphic_tree.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Entity",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "date_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "date_modified",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "creator",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "parent",
                    polymorphic_tree.models.PolymorphicTreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="www.entity",
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_www.entity_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tree node",
                "verbose_name_plural": "Tree nodes",
                "ordering": ("tree_id", "lft"),
                "abstract": False,
                "base_manager_name": "objects",
            },
        ),
        migrations.CreateModel(
            name="Attachment",
            fields=[
                (
                    "entity_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="www.entity",
                    ),
                ),
                ("file_name", models.CharField(max_length=255)),
                ("file_type", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ("tree_id", "lft"),
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("www.entity",),
        ),
        migrations.CreateModel(
            name="MarkdownEntity",
            fields=[
                (
                    "entity_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="www.entity",
                    ),
                ),
                (
                    "markdown",
                    markdownfield.models.MarkdownField(
                        default="", rendered_field="content_rendered", use_editor=False
                    ),
                ),
                (
                    "markdown_rendered",
                    markdownfield.models.RenderedMarkdownField(default=""),
                ),
            ],
            options={
                "ordering": ("tree_id", "lft"),
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("www.entity",),
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "entity_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        to="www.entity",
                    ),
                ),
                (
                    "key",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
            ],
            options={
                "ordering": ("tree_id", "lft"),
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("www.entity",),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "markdownentity_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="www.markdownentity",
                    ),
                ),
            ],
            options={
                "ordering": ("tree_id", "lft"),
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("www.markdownentity",),
        ),
        migrations.CreateModel(
            name="JournalPage",
            fields=[
                (
                    "markdownentity_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="www.markdownentity",
                    ),
                ),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "ordering": ("tree_id", "lft"),
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("www.markdownentity",),
        ),
        migrations.CreateModel(
            name="WikiPage",
            fields=[
                (
                    "markdownentity_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="www.markdownentity",
                    ),
                ),
            ],
            options={
                "ordering": ("tree_id", "lft"),
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("www.markdownentity",),
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "markdownentity_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="www.markdownentity",
                    ),
                ),
                ("due_date", models.DateTimeField(null=True)),
                ("content", models.TextField()),
                (
                    "assignee",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="Assignee",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("tree_id", "lft"),
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("www.markdownentity",),
        ),
    ]
