from django.views.generic import ListView
from django.contrib.auth import get_user_model

User = get_user_model()


class PeopleDirectory(ListView):
    model = User
    template_name = "www/snippets/people.html"
    context_object_name = "users"
