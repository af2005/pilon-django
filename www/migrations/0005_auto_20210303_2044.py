# Generated by Django 3.1.7 on 2021-03-03 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('www', '0004_auto_20210215_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='content',
        ),
        migrations.AlterField(
            model_name='entity',
            name='creator',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entities', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
