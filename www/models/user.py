from django.contrib.auth import models as auth_models

from www.models.mixins import RandomUUIDMixin


class User(auth_models.AbstractUser, RandomUUIDMixin):
    pass


class Group(auth_models.Group, RandomUUIDMixin):
    pass