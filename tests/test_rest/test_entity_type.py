from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
class TestEntityType:
    client = APIClient()

    @pytest.fixture(autouse=True)
    def setup_login(self, db):
        self.client.login(username="TestUser", password="password")

    def test_get_wikipage(self):
        response = self.client.get("/rest/wiki-page/")
        assert response.status_code == 200

    def test_missing_entity_type(self):
        response = self.client.post("/rest/wiki-page/", data={"name": "new page"})
        assert response.status_code == 201
        assert response.data["entity_type"] == "WikiPage"

    def test_wrong_entity_type(self):
        response = self.client.post(
            "/rest/wiki-page/", data={"name": "new page", "entity_type": "JournalPage"}
        )
        assert response.status_code == 201
        assert response.data["entity_type"] == "WikiPage"
