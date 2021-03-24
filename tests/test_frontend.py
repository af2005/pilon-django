from django.test import Client
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from www.models import Project

from django.urls import reverse

TEST_PROJECT_KEY = "testproject"


class TestFrontend(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="testuser", password="top_secret"
        )
        self.client = Client()
        login = self.client.login(username="testuser", password="top_secret")
        self.assertTrue(login)
        self.project = Project.objects.create(
            key=TEST_PROJECT_KEY, name="This is a test project"
        )

    def test_default_views(self):
        default_views = [
            "View Dashboard",
            "All updates board",
            "Last worked on board",
            "User settings",
            "View People",
            "Create Project",
            "Project Directory",
        ]
        for view in default_views:
            reversed_url = reverse(view)
            response = self.client.get(reversed_url)
            self.assertEqual(response.status_code, 200)

    def test_project_views(self):
        project_views = [
            "project:homepage",
            "project:create-child-entity",
            "project:tasks",
            "project:chat",
            "project:tasks",
            "project:calendar",
            "project:inventory",
            "project:wiki",
            "project:create-wiki-page",
            "project:create-wiki-page-from-file",
            "project:journal",
            "project:create-journal-page",
            "project:create-journal-page-from-file",
        ]
        for view in project_views:
            reversed_url = reverse(view, kwargs={"key": TEST_PROJECT_KEY})
            response = self.client.get(reversed_url)
            self.assertEqual(response.status_code, 200)
