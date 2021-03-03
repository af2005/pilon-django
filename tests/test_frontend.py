from django.contrib.auth import get_user_model, models
from django.http import HttpResponse
from django.test import TestCase, Client
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
import unittest
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
        DEFAULT_VIEWS = [
            "View Dashboard",
            "All updates board",
            "Last worked on board",
            "User settings",
            "View People",
            "Create Project",
            "Project Directory",
        ]
        for view in DEFAULT_VIEWS:
            reversed_url = reverse(view)
            response = self.client.get(reversed_url)
            self.assertEqual(response.status_code, 200)

    def test_project_views(self):
        PROJECT_VIEWS = [
            "Project Homepage",
            "Create Content",
            "Project Tasks",
            "Project Chat",
            "Project Tasks",
            "Project Calendar",
            "Project Inventory",
            "Project Wiki",
            "Create Wiki Page",
            "Create Wiki Page with file",
            "Project Journal",
            "Create Journal Page",
            "Create Journal Page with file",
        ]
        for view in PROJECT_VIEWS:
            reversed_url = reverse(view, kwargs={"key": TEST_PROJECT_KEY})
            response = self.client.get(reversed_url)
            self.assertEqual(response.status_code, 200)
