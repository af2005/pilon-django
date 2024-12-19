from django.contrib.auth import models as auth_models

from www.models.mixins import ShortUUIDMixin


class User(auth_models.AbstractUser, ShortUUIDMixin):
    pass


class Group(auth_models.Group):
    pass
