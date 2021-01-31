from django.contrib.auth.models import User


def list_all_users():
    return User.objects.get()
