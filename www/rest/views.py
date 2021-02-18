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


# TODO: add permission
class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntityPolymorphicSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = EntityPolymorphicSerializer


class MarkdownEntityViewSet(viewsets.ModelViewSet):
    queryset = MarkdownEntity.objects.all()
    serializer_class = EntityPolymorphicSerializer


class WikiPageViewSet(viewsets.ModelViewSet):
    queryset = WikiPage.objects.all()
    serializer_class = EntityPolymorphicSerializer


class JournalPageViewSet(viewsets.ModelViewSet):
    queryset = JournalPage.objects.all()
    serializer_class = EntityPolymorphicSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = EntityPolymorphicSerializer


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = EntityPolymorphicSerializer
