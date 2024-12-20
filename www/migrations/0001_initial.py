# Generated by Django 3.2 on 2021-04-16 00:10

import colorfield.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import markdownfield.models
import shortuuid.main
import shortuuidfield.fields
import www.models.entity


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={"unique": "A user with that username already exists."},
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(blank=True, max_length=150, verbose_name="first name"),
                ),
                (
                    "last_name",
                    models.CharField(blank=True, max_length=150, verbose_name="last name"),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=254, verbose_name="email address"),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("pkid", models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                (
                    "id",
                    shortuuidfield.fields.ShortUUIDField(
                        blank=True,
                        default=shortuuid.main.ShortUUID.uuid,
                        editable=False,
                        max_length=22,
                        unique=True,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Entity",
            fields=[
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(editable=False)),
                ("pkid", models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                (
                    "id",
                    shortuuidfield.fields.ShortUUIDField(
                        blank=True,
                        default=shortuuid.main.ShortUUID.uuid,
                        editable=False,
                        max_length=22,
                        unique=True,
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(default=django.utils.timezone.now, editable=False),
                ),
                ("date_modified", models.DateTimeField(default=django.utils.timezone.now)),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="created_entities",
                        to=settings.AUTH_USER_MODEL,
                        to_field="id",
                    ),
                ),
                (
                    "parent",
                    www.models.entity.ShortUUIDPolymorphicTreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="www.entity",
                        to_field="id",
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
                "verbose_name": "Entity",
                "verbose_name_plural": "Entities",
                "ordering": ("tree_id", "lft"),
                "abstract": False,
                "base_manager_name": "objects",
            },
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "group_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="auth.group",
                    ),
                ),
            ],
            bases=("auth.group",),
            managers=[
                ("objects", django.contrib.auth.models.GroupManager()),
            ],
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
                ("file_path", models.CharField(max_length=255)),
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
                        blank=True,
                        default="",
                        rendered_field="markdown_rendered",
                        use_admin_editor=False,
                        use_editor=False,
                    ),
                ),
                ("markdown_rendered", markdownfield.models.RenderedMarkdownField(default="")),
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
                        primary_key=True,
                        serialize=False,
                        to="www.entity",
                    ),
                ),
                ("key", models.CharField(max_length=20, unique=True)),
                (
                    "color",
                    colorfield.fields.ColorField(blank=True, default="#FF0000", max_length=18),
                ),
            ],
            options={
                "verbose_name": "Project",
                "verbose_name_plural": "Projects",
                "ordering": ("tree_id", "lft"),
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("www.entity",),
        ),
        migrations.CreateModel(
            name="Label",
            fields=[
                ("slug", models.SlugField(editable=False)),
                ("pkid", models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                (
                    "id",
                    shortuuidfield.fields.ShortUUIDField(
                        blank=True,
                        default=shortuuid.main.ShortUUID.uuid,
                        editable=False,
                        max_length=22,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "entities",
                    models.ManyToManyField(blank=True, related_name="labels", to="www.Entity"),
                ),
            ],
            options={
                "abstract": False,
            },
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
                "verbose_name": "Wiki Page",
                "verbose_name_plural": "Wiki Pages",
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
                ("due_date", models.DateTimeField(blank=True, null=True)),
                (
                    "assignee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="tasks",
                        to=settings.AUTH_USER_MODEL,
                        to_field="id",
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
