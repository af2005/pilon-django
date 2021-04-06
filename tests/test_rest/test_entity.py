from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
class TestEntity:
    client = APIClient()

    @pytest.fixture(autouse=True)
    def setup_login(self, db):
        self.client.login(username="TestUser", password="password")

    def test_get(self):
        response = self.client.get("/rest/entity/")
        assert response.status_code == 200

    # TODO:10 Fix with issue #84
    @pytest.mark.xfail(reason="needs fixing")
    def test_parent_url_not_entity(self):
        parent_url = self.client.get("/rest/project/").data[0]["url"]
        data = {"name": "entity1", "entities": [parent_url]}
        response = self.client.post("/rest/entity/", data=data, format="json")
        print(response.data)
        assert response.status_code == 201
