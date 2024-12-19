from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase, Client
from www.models.entity import Project

from django.urls import reverse

TEST_PROJECT_KEY = "testproject"

User = get_user_model()


class TestFrontend(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(username="testuser", password="top_secret")
        self.client = Client()
        login = self.client.login(username="testuser", password="top_secret")
        self.assertTrue(login)
        self.project = Project.objects.create(key=TEST_PROJECT_KEY, name="This is a test project")

    def test_default_views(self):
        default_views = [
            "dashboard:home",
            "dashboard:all-updates",
            "dashboard:last-worked-on",
            "user-settings",
            "people-list",
            "project-create",
            "project-directory",
        ]
        for view in default_views:
            with self.subTest(view=view):
                reversed_url = reverse(view)
                response = self.client.get(reversed_url)
                self.assertEqual(response.status_code, 200)

    def test_project_views(self):
        project_views = [
            "project:home",
            "project:child-entity-create",
            "project:tasks",
            "project:chat",
            "project:tasks",
            "project:calendar",
            "project:inventory",
            "project:wiki",
            "project:wiki-page-create",
            "project:wiki-page-create-from-file",
            "project:journal",
            "project:journal-page-create",
            "project:journal-page-create-from-file",
        ]
        for view in project_views:
            with self.subTest(view=view):
                reversed_url = reverse(view, kwargs={"key": TEST_PROJECT_KEY})
                response = self.client.get(reversed_url)
                self.assertEqual(response.status_code, 200)
