from ..models import User


def list_all_users():
    return [user for user in User.objects.all()]
