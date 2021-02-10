from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from unittest import skip
from www.screens.dashboard.main import (
    view_dashboard,
    view_all_updates_board,
    view_recently_worked_on_board,
)


@skip
class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="jacob", email="jacob@…", password="top_secret"
        )

    def test_dashboard(self):
        # Create an instance of a GET request.
        request = self.factory.get("/")

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = view_dashboard(request)
        print(response)
