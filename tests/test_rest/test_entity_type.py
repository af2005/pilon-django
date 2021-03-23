from rest_framework.test import APIRequestFactory, APIClient
import pytest


# Using the standard RequestFactory API to create a form POST request


@pytest.mark.django_db
class TestEntityType:
    factory = APIRequestFactory()
    client = APIClient()

    def test_missing_entity_type(self):
        self.client.login(username="admin", password="password")
        response = self.client.get("/rest/wiki-page/")
        print(response)

    def test_wrong_entity_type(self):
        self.client.login(username="admin", password="passwort")
        response = self.client.get("/rest/wiki-page/")
        print(response)
