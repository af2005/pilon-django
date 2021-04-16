from rest_framework import serializers
from www.models.entity import (
    Entity,
    Project,
    MarkdownEntity,
    WikiPage,
    JournalPage,
    Task,
    Comment,
    Attachment,
)
from www.models.label import Label
from www.models.user import Group
from www.models.mixins import ShortUUIDMixin
from rest_polymorphic.serializers import PolymorphicSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ShortUUIDHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShortUUIDMixin

    def __init_subclass__(cls, **kwargs):
        try:
            cls.url = serializers.HyperlinkedIdentityField(
                view_name=f"{cls.Meta.model.url_base}-detail",
                lookup_field="id",
                lookup_url_kwarg="id",
                read_only=True,
            )
        except AttributeError:
            AttributeError(
                f"Serializer needs a class Meta with a model that inherits from {ShortUUIDMixin.__qualname__}."
            )
        super().__init_subclass__(**kwargs)
        print(f"{cls}:{cls.url}")

    def get_extra_kwargs(self):
        extra_kwargs = super().get_extra_kwargs()
        url = {
            "url": {
                "view_name": f"{self.Meta.model.__name__.lower()}-detail",
                "lookup_field": "id",
                "lookup_url_kwarg": "id",
            }
        }
        return {
            **url,
            **extra_kwargs,
        }


class UserSerializer(ShortUUIDHyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(
        lookup_field="id",
        lookup_url_kwarg="id",
        many=True,
        read_only=True,
        required=False,
        view_name="task-detail",
    )
    created_entities = serializers.HyperlinkedRelatedField(
        lookup_field="id",
        lookup_url_kwarg="id",
        many=True,
        read_only=True,
        required=False,
        view_name="entity-detail",
    )

    groups = serializers.HyperlinkedRelatedField(
        lookup_field="id",
        lookup_url_kwarg="id",
        many=True,
        read_only=False,
        required=False,
        view_name="group-detail",
        queryset=Group.objects.all(),
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
    url = serializers.HyperlinkedIdentityField(
        view_name="group-detail", lookup_field="id", lookup_url_kwarg="id"
    )

    class Meta:
        model = Group
        fields = ["url", "id", "name"]


class LabelSerializer(ShortUUIDHyperlinkedModelSerializer):
    entities = serializers.HyperlinkedRelatedField(
        lookup_field="id",
        lookup_url_kwarg="id",
        many=True,
        queryset=Entity.objects.all(),
        required=False,
        view_name="entity-detail",
    )

    class Meta:
        model = Label
        fields = ["url", "name", "slug", "entities"]


class EntitySerializer(ShortUUIDHyperlinkedModelSerializer):
    children = serializers.HyperlinkedRelatedField(
        lookup_field="id",
        lookup_url_kwarg="id",
        many=True,
        read_only=True,
        required=False,
        view_name="entity-detail",
    )

    labels = serializers.HyperlinkedRelatedField(
        lookup_field="id",
        lookup_url_kwarg="id",
        many=True,
        required=False,
        view_name="label-detail",
        queryset=Label.objects.all(),
    )

    creator = serializers.HyperlinkedRelatedField(
        lookup_field="id",
        lookup_url_kwarg="id",
        many=False,
        required=False,
        view_name="user-detail",
        queryset=User.objects.all(),
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


class ProjectSerializer(EntitySerializer):
    class Meta:
        model = Project
        fields = EntitySerializer.Meta.fields + ("key", "color")


class MarkdownEntitySerializer(EntitySerializer):
    class Meta:
        model = MarkdownEntity
        fields = EntitySerializer.Meta.fields + ("markdown", "markdown_rendered")


class WikiPageSerializer(MarkdownEntitySerializer):
    class Meta:
        model = WikiPage
        fields = MarkdownEntitySerializer.Meta.fields


class JournalPageSerializer(MarkdownEntitySerializer):
    class Meta:
        model = JournalPage
        fields = MarkdownEntitySerializer.Meta.fields + ("date",)


class TaskSerializer(MarkdownEntitySerializer):
    assignee = serializers.HyperlinkedRelatedField(
        lookup_field="id",
        lookup_url_kwarg="id",
        many=False,
        required=False,
        view_name="user-detail",
        queryset=User.objects.all(),
    )

    class Meta:
        model = Task
        fields = MarkdownEntitySerializer.Meta.fields + ("due_date", "assignee")


class CommentSerializer(MarkdownEntitySerializer):
    class Meta:
        model = Comment
        fields = MarkdownEntitySerializer.Meta.fields


class AttachmentSerializer(EntitySerializer):
    class Meta:
        model = Attachment
        fields = EntitySerializer.Meta.fields + ("file_name", "file_type", "file_path")


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
