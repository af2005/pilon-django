from rest_framework import serializers
from ..models import (
    User,
    Group,
    Entity,
    Project,
    MarkdownEntity,
    WikiPage,
    JournalPage,
    Task,
    Comment,
    Attachment,
    Label,
)
from rest_polymorphic.serializers import PolymorphicSerializer
from django.urls import reverse


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, required=False, view_name="task-detail"
    )
    created_entities = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, required=False, view_name="entity-detail"
    )

    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "username",
            "email",
            "groups",
            "tasks",
            "created_entities",
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "id", "name"]


class EntityHyperlink(serializers.HyperlinkedRelatedField):
    # We define these as class attributes, so we don't need to pass them as arguments.
    view_name = "customer-detail"
    queryset = Entity.objects.all()
    many = True
    required = False

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {"organization_slug": obj.organization.slug, "customer_pk": obj.pk}
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            "organization__slug": view_kwargs["organization_slug"],
            "pk": view_kwargs["customer_pk"],
        }
        return self.get_queryset().get(**lookup_kwargs)


class LabelSerializer(serializers.HyperlinkedModelSerializer):
    entities = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=Entity.objects.all(),
        required=False,
        view_name="entity-detail",
    )

    class Meta:
        model = Label
        fields = ["url", "name", "slug", "entities"]

        # extra_kwargs = {'url': {'lookup_field': 'slug'}}


class EntitySerializer(serializers.HyperlinkedModelSerializer):
    children = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, required=False, view_name="entity-detail"
    )

    class Meta:
        model = Entity
        fields = (
            "url",
            "id",
            "name",
            "parent",
            "date_created",
            "date_modified",
            "creator",
            "children",
            "labels",
        )
        extra_kwargs = {
            "creator": {"view_name": "user-detail", "lookup_field": "pk"},
            "labels": {"view_name": "label-detail", "lookup_field": "slug"},
        }


class ProjectSerializer(EntitySerializer):
    class Meta:
        model = Project
        fields = EntitySerializer.Meta.fields + ("key", "color")
        extra_kwargs = EntitySerializer.Meta.extra_kwargs


class MarkdownEntitySerializer(EntitySerializer):
    class Meta:
        model = MarkdownEntity
        fields = EntitySerializer.Meta.fields + ("markdown", "markdown_rendered")
        extra_kwargs = EntitySerializer.Meta.extra_kwargs


class WikiPageSerializer(MarkdownEntitySerializer):
    class Meta:
        model = WikiPage
        fields = MarkdownEntitySerializer.Meta.fields
        extra_kwargs = MarkdownEntitySerializer.Meta.extra_kwargs


class JournalPageSerializer(MarkdownEntitySerializer):
    class Meta:
        model = JournalPage
        fields = MarkdownEntitySerializer.Meta.fields + ("date",)
        extra_kwargs = MarkdownEntitySerializer.Meta.extra_kwargs


class TaskSerializer(MarkdownEntitySerializer):
    class Meta:
        model = Task
        fields = MarkdownEntitySerializer.Meta.fields + ("due_date", "assignee")
        extra_kwargs = {
            **MarkdownEntitySerializer.Meta.extra_kwargs,
            **{
                "assignee": {"view_name": "user-detail", "lookup_field": "pk"},
            },
        }


class CommentSerializer(MarkdownEntitySerializer):
    class Meta:
        model = Comment
        fields = MarkdownEntitySerializer.Meta.fields
        extra_kwargs = EntitySerializer.Meta.extra_kwargs


class AttachmentSerializer(EntitySerializer):
    class Meta:
        model = Attachment
        fields = EntitySerializer.Meta.fields + ("file_name", "file_type", "file_path")
        extra_kwargs = EntitySerializer.Meta.extra_kwargs


class EntityPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = "entity_type"
    model_serializer_mapping = {
        Entity: EntitySerializer,
        Project: ProjectSerializer,
        MarkdownEntity: MarkdownEntitySerializer,
        WikiPage: WikiPageSerializer,
        JournalPage: JournalPageSerializer,
        Task: TaskSerializer,
        Comment: CommentSerializer,
        Attachment: AttachmentSerializer,
    }

    # def to_resource_type(self, model_or_instance):
    #     return model_or_instance._meta.object_name.lower()
