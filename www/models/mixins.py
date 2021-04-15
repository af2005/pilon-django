import shortuuid
from django.db import models
from django.utils.text import slugify
from shortuuidfield import ShortUUIDField


class SluggedNameMixin(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class RandomUUIDMixin(models.Model):
    id = ShortUUIDField(primary_key=True, default=shortuuid.uuid)

    class Meta:
        abstract = True
