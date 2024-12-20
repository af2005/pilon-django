from rest_framework import viewsets, permissions
from ..models.entity import (
    Entity,
    Project,
    MarkdownEntity,
    WikiPage,
    JournalPage,
    Task,
    Comment,
    Attachment,
)
from ..models.label import Label
from ..models.user import Group
from .serializers import (
    EntityPolymorphicSerializer,
    UserSerializer,
    GroupSerializer,
    LabelSerializer,
)
from django.contrib.auth import get_user_model

User = get_user_model()

# https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups
DATETIME_FIELD_LOOKUPS = ["exact", "date", "date__range", "gte", "lte"]


class ShortUUIDModelViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    lookup_url_kwarg = "id"

    # pass


class UserViewSet(ShortUUIDModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = (
        "id",
        "username",
        "email",
        "groups",
        "tasks",
        "created_entities",
    )


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ("id", "name")
    lookup_field = "id"


class LabelViewSet(ShortUUIDModelViewSet):
    """
    API endpoint that allows labels to be viewed or edited.
    """

    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    filterset_fields = ["name", "slug", "entities"]


# TODO:10 add permission
class EntityViewSet(ShortUUIDModelViewSet):
    model = Entity
    queryset = model.objects.all()
    serializer_class = EntityPolymorphicSerializer
    filterset_fields = {
        "id": ["exact"],
        "name": ["exact"],
        "parent": ["exact"],
        "date_created": DATETIME_FIELD_LOOKUPS,
        "date_modified": DATETIME_FIELD_LOOKUPS,
        "creator": ["exact"],
        "children": ["exact"],
        "labels": ["exact"],
    }
    # search_fields = ("id", "name", "date_modified")

    # inspired by: https://www.valentinog.com/blog/drf-request/
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs.setdefault("context", self.get_serializer_context())
        # Copy and manipulate the request
        if self.request.method != "GET" and kwargs.get("data"):
            draft_request_data = self.request.data.copy()
            draft_request_data["entity_type"] = self.model.__name__
            kwargs["data"] = draft_request_data
            serializer = serializer_class(*args, **kwargs)
            return serializer
        return serializer_class(*args, **kwargs)


class ProjectViewSet(EntityViewSet):
    model = Project
    queryset = model.objects.all()
    filterset_fields = {"key": ["exact"], "color": ["exact"], **EntityViewSet.filterset_fields}


class MarkdownEntityViewSet(EntityViewSet):
    model = MarkdownEntity
    queryset = model.objects.all()
    filterset_fields = {
        "markdown": ["exact"],
        "markdown_rendered": ["exact"],
        **EntityViewSet.filterset_fields,
    }


class WikiPageViewSet(EntityViewSet):
    model = WikiPage
    queryset = model.objects.all()


class JournalPageViewSet(EntityViewSet):
    model = JournalPage
    queryset = model.objects.all()
    # https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups
    filterset_fields = {"date": DATETIME_FIELD_LOOKUPS, **MarkdownEntityViewSet.filterset_fields}
    ordering = ("date",)


class TaskViewSet(EntityViewSet):
    model = Task
    queryset = model.objects.all()
    filterset_fields = {
        "due_date": DATETIME_FIELD_LOOKUPS,
        "assignee": ["exact"],
        **MarkdownEntityViewSet.filterset_fields,
    }


class CommentViewSet(EntityViewSet):
    model = Comment
    queryset = model.objects.all()


class AttachmentViewSet(EntityViewSet):
    model = Attachment
    queryset = model.objects.all()
    filterset_fields = {
        "file_name": ["exact"],
        "file_type": ["exact"],
        "file_path": ["exact"],
        **EntityViewSet.filterset_fields,
    }
