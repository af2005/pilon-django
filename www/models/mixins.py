import inflection
import shortuuid
from django.db import models
from django.utils.text import slugify
from shortuuidfield import ShortUUIDField
from django.db.models.fields import AutoField


# this is not working currently, but might with PR https://code.djangoproject.com/ticket/32577
class RandomUUIDAutoField(AutoField):
    def get_pk_value_on_save(self, instance):
        return shortuuid.uuid()


class SluggedNameMixin(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ShortUUIDMixin(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = ShortUUIDField(default=shortuuid.uuid, editable=False, unique=True)

    url_base = ""

    def __init_subclass__(cls, **kwargs):
        cls.url_base = inflection.dasherize(inflection.underscore(cls.__name__))

    class Meta:
        abstract = True
