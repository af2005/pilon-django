# Generated by Django 3.2 on 2021-04-10 20:41

from django.db import migrations
import shortuuid.main
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0006_auto_20210410_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='label',
            name='id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
    ]
