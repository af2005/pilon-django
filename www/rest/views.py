from rest_framework import viewsets, permissions
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
)
from .serializers import EntityPolymorphicSerializer, UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# TODO:0 add permission
class EntityViewSet(viewsets.ModelViewSet):
    model = Entity
    queryset = model.objects.all()
    serializer_class = EntityPolymorphicSerializer

    # def get_queryset(self):
    #     return self.model.objects.all()

    # inspired by: https://www.valentinog.com/blog/drf-request/
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs.setdefault("context", self.get_serializer_context())
        print("called get serialiser")
        # Copy and manipulate the request
        if self.request.method != "GET":
            draft_request_data = self.request.data.copy()
            if draft_request_data:
                draft_request_data["entity_type"] = self.model.__name__
                kwargs["data"] = draft_request_data
                serializer = serializer_class(*args, **kwargs)
                serializer.is_valid()
                serializer.save()
                return serializer
        return serializer_class(*args, **kwargs)

        # Copy and manipulate the request
        if self.request.method != "GET":
            draft_request_data = self.request.data.copy()
            if draft_request_data:
                draft_request_data["entity_type"] = self.model.__name__
                kwargs["data"] = draft_request_data
                serializer = serializer_class(*args, **kwargs)
                serializer.is_valid()
                return serializer

class ProjectViewSet(EntityViewSet):
    model = Project
    queryset = model.objects.all()


class MarkdownEntityViewSet(EntityViewSet):
    model = MarkdownEntity
    queryset = model.objects.all()


class WikiPageViewSet(EntityViewSet):
    model = WikiPage
    queryset = model.objects.all()


class JournalPageViewSet(EntityViewSet):
    model = JournalPage
    queryset = model.objects.all()


class TaskViewSet(EntityViewSet):
    model = Task
    queryset = model.objects.all()


class CommentViewSet(EntityViewSet):
    model = Comment
    queryset = model.objects.all()


class AttachmentViewSet(EntityViewSet):
    model = Attachment
    queryset = model.objects.all()
