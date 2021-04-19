import reversion
from django.db import models

from www.models.entity import Entity
from www.models.mixins import ShortUUIDMixin, SluggedNameMixin


@reversion.register()
class Label(SluggedNameMixin, ShortUUIDMixin):
    name = models.CharField(unique=True, max_length=50)
    entities = models.ManyToManyField(Entity, related_name="labels", blank=True)
