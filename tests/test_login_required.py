from django.contrib.auth.models import AnonymousUser, User
from django.test import Client, TestCase
from unittest import skip
from www.views.dashboard.dashboard_views import (
    view_dashboard,
    view_all_updates_board,
    view_recently_worked_on_board,
)


class TestLoginRequired(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.client = Client()
        self.user = User.objects.create_user(
            username="user", email="testuser@email.com", password="password"
        )

    def test_not_logged_in(self):
        response = self.client.get("/")
        assert 302 == response.status_code

    def test_logged_in(self):
        self.client.login(username='user', password='password')
        response = self.client.get("/")
        assert 200 == response.status_code
