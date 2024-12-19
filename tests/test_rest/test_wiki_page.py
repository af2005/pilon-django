from rest_framework.test import APIClient
import pytest
import json


@pytest.mark.django_db
class TestWikiPage:
    client = APIClient()

    @pytest.fixture(autouse=True)
    def setup_login(self, db):
        self.client.login(username="TestUser", password="password")

    def test_get(self):
        response = self.client.get("/rest/wiki-page/")
        assert response.status_code == 200
