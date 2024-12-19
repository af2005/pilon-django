from django.contrib.auth import get_user_model
from django.test import Client, TestCase

User = get_user_model()


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
        self.client.login(username="user", password="password")
        response = self.client.get("/")
        assert 200 == response.status_code
