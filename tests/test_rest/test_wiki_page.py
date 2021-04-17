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
        response = self.client.get("/rest/entity/")
        assert response.status_code == 200

    def test_post_only_creating_one(self):
        pages_before = len(self.client.get("/rest/wiki-page/").json())
        response = self.client.post(
            "/rest/wiki-page/",
            data=json.dumps({"name": "new page", "labels": []}),
            content_type="application/json",
        )
        pages_after = len(self.client.get("/rest/wiki-page/").json())
        assert response.status_code == 201
        assert pages_after == pages_before + 1
