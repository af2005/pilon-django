from rest_framework import serializers
from ..models import Entity, Project, MarkdownEntity, Task, Attachment
from rest_polymorphic.serializers import PolymorphicSerializer


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ("id", "name", "parent", "date_created", "date_modified", "creator")


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "key"


class MarkdownEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkdownEntity
        fields = ("markdown", "markdown_rendered")


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("due_date", "assignee")


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ("file_name", "file_type", "file_path")


class ProjectPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Entity: EntitySerializer,
        Project: ProjectSerializer,
        MarkdownEntity: MarkdownEntitySerializer,
        Task: TaskSerializer,
        Attachment: AttachmentSerializer,
    }
