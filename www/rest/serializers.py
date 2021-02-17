from rest_framework import serializers
from ..models import User, Group, Entity, Project, MarkdownEntity, WikiPage, JournalPage, Task, Attachment
from rest_polymorphic.serializers import PolymorphicSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups", "tasks", "created"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class EntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entity
        fields = ("url", "name", "parent", "date_created", "date_modified", "creator", "children")
        extra_kwargs = {
            "creator": {"view_name": "user-detail", "lookup_field": "pk"},
        }


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = EntitySerializer.Meta.fields + ("key",)
        extra_kwargs = EntitySerializer.Meta.extra_kwargs


class MarkdownEntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarkdownEntity
        fields = EntitySerializer.Meta.fields + ("markdown", "markdown_rendered")
        extra_kwargs = EntitySerializer.Meta.extra_kwargs


class WikiPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WikiPage
        fields = EntitySerializer.Meta.fields
        extra_kwargs = EntitySerializer.Meta.extra_kwargs


class JournalPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JournalPage
        fields = EntitySerializer.Meta.fields + ("date", )
        extra_kwargs = EntitySerializer.Meta.extra_kwargs


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = EntitySerializer.Meta.fields + ("due_date", "assignee")
        extra_kwargs = EntitySerializer.Meta.extra_kwargs | {
            "assignee": {"view_name": "user-detail", "lookup_field": "pk"},
        }


class AttachmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attachment
        fields = EntitySerializer.Meta.fields + ("file_name", "file_type", "file_path")
        extra_kwargs = EntitySerializer.Meta.extra_kwargs


class EntityPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = 'entity_type'
    model_serializer_mapping = {
        Entity: EntitySerializer,
        Project: ProjectSerializer,
        MarkdownEntity: MarkdownEntitySerializer,
        WikiPage: MarkdownEntitySerializer,
        JournalPage: JournalPageSerializer,
        Task: TaskSerializer,
        Attachment: AttachmentSerializer,
    }
