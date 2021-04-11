from rest_framework.test import APIClient
import pytest

from www.models.label import Label


@pytest.mark.django_db
class TestLabel:
    client = APIClient()

    @pytest.fixture(autouse=True)
    def setup_login(self, db):
        self.client.login(username="admin", password="password")

    def test_get_label(self):
        Label(name="label1").save()
        response = self.client.get("/rest/label/")
        assert response.status_code == 200
        label = response.data[0]
        assert label["name"] == "label1"

    def test_post_label(self):
        response = self.client.post("/rest/label/", data={"name": "label1"}, format="json")
        assert response.status_code == 201

    # TODO:20 Fix with issue #84
    @pytest.mark.xfail(reason="needs fixing")
    def test_post_label_with_entity(self):
        entity = self.client.get("/rest/entity/").data[0]
        print(f"entity_url = {entity['url']}")
        data = {"name": "label2", "entities": [entity["url"]]}
        response = self.client.post("/rest/label/", data=data, format="json")
        print(response.data)
        assert response.status_code == 201

    def test_slug(self):
        Label(name="label with space").save()
        response = self.client.get("/rest/label/")
        assert response.status_code == 200
        label = response.data[0]
        assert label["slug"] == "label-with-space"
        assert label["name"] == "label with space"

        # change label name to not include spaces
        response = self.client.patch(label["url"], data={"name": "labelnospace"})
        response = self.client.get("/rest/label/")
        assert response.status_code == 200
        label = response.data[0]
        assert label["slug"] == "labelnospace"

    def test_same_name(self):
        Label(name="label with space").save()
        Label(name="label-with-space").save()

    def test_minus_name(self):
        Label(name="1").save()
        Label(name="-1").save()

    def test_special_characters(self):
        Label(name="&").save()
        Label(name="/").save()
        Label(name="?").save()
