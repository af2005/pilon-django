# Generated by Django 3.1.6 on 2021-02-14 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("www", "0002_populate"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="entity",
            options={
                "base_manager_name": "objects",
                "ordering": ("tree_id", "lft"),
                "verbose_name": "Entity",
                "verbose_name_plural": "Entities",
            },
        ),
        migrations.AlterModelOptions(
            name="project",
            options={
                "base_manager_name": "objects",
                "ordering": ("tree_id", "lft"),
                "verbose_name": "Project",
                "verbose_name_plural": "Projects",
            },
        ),
        migrations.AlterModelOptions(
            name="wikipage",
            options={
                "base_manager_name": "objects",
                "ordering": ("tree_id", "lft"),
                "verbose_name": "Wiki Page",
                "verbose_name_plural": "Wiki Pages",
            },
        ),
        migrations.AlterField(
            model_name="entity",
            name="creator",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="EntityCreator",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
