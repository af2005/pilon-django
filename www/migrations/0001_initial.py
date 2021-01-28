# Generated by Django 3.1.5 on 2021-01-28 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('version', models.IntegerField()),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('full_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JournalPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='www.page')),
                ('date', models.DateTimeField()),
            ],
            bases=('www.page',),
        ),
        migrations.CreateModel(
            name='WikiPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='www.page')),
            ],
            bases=('www.page',),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
                ('content', models.TextField()),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Assignee', to='www.user')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reporter', to='www.user')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.project'),
        ),
    ]
