# Generated by Django 3.1.6 on 2021-02-11 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import markdownfield.models
import mptt.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('ENTITY_TYPE', models.CharField(default='Entity', max_length=255)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='contenttypes.contenttype')),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='www.entity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='www.entity')),
                ('file_name', models.CharField(max_length=255)),
                ('file_type', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('www.entity',),
        ),
        migrations.CreateModel(
            name='MarkdownEntity',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='www.entity')),
                ('markdown', markdownfield.models.MarkdownField(default='', rendered_field='content_rendered', use_editor=False)),
                ('markdown_rendered', markdownfield.models.RenderedMarkdownField(default='')),
            ],
            options={
                'abstract': False,
            },
            bases=('www.entity',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='www.entity')),
                ('key', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('www.entity',),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('markdownentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='www.markdownentity')),
            ],
            options={
                'abstract': False,
            },
            bases=('www.markdownentity',),
        ),
        migrations.CreateModel(
            name='JournalPage',
            fields=[
                ('markdownentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='www.markdownentity')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
            bases=('www.markdownentity',),
        ),
        migrations.CreateModel(
            name='WikiPage',
            fields=[
                ('markdownentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='www.markdownentity')),
            ],
            options={
                'abstract': False,
            },
            bases=('www.markdownentity',),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('markdownentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='www.markdownentity')),
                ('due_date', models.DateTimeField(null=True)),
                ('content', models.TextField()),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Assignee', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('www.markdownentity',),
        ),
    ]
