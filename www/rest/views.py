from rest_framework import viewsets
from ..models import Entity, Project, MarkdownEntity, Task, Attachment
from .serializers import ProjectPolymorphicSerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = ProjectPolymorphicSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectPolymorphicSerializer


class MarkdownEntityViewSet(viewsets.ModelViewSet):
    queryset = MarkdownEntity.objects.all()
    serializer_class = ProjectPolymorphicSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = ProjectPolymorphicSerializer


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = ProjectPolymorphicSerializer
