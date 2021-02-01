from django.contrib.auth.models import User


def list_all_users():
    users = []
    for user in User.objects.all():
        users.append(user)
    return users
