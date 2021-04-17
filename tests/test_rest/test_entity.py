from rest_framework.test import APIClient
import pytest
import json


@pytest.mark.django_db
class TestEntity:
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

    def test_absolute_url(self):
        response = self.client.get("/rest/entity/")
        assert response.status_code == 200
        print(response.json())

    # TODO:10 Fix with issue #84
    @pytest.mark.xfail(reason="needs fixing")
    def test_parent_url_not_entity(self):
        parent_url = self.client.get("/rest/project/").data[0]["url"]
        data = {"name": "entity1", "parent": parent_url}
        response = self.client.post("/rest/entity/", data=data, format="json")
        assert response.status_code == 201


@pytest.mark.django_db
class TestAbsoluteURL:
    client = APIClient()

    @pytest.fixture(autouse=True)
    def setup_login(self, db):
        self.client.login(username="TestUser", password="password")

    def test_project(self):
        response = self.client.get("/rest/project/")
        assert response.status_code == 200
        for project in response.data:
            assert project["absolute_url"] == f"http://testserver/project/{project['key']}/"

    def test_wiki_page(self):
        response = self.client.get("/rest/wiki-page/")
        assert response.status_code == 200
        for wiki_page in response.data:
            print(wiki_page)
            # assert wiki_page["absolute_url"] == f"http://testserver/project/test/wiki/view/{wiki_page['id']}/"

    def test_journal_page(self):
        response = self.client.get("/rest/journal-page/")
        assert response.status_code == 200
        for journal_page in response.data:
            assert (
                journal_page["absolute_url"]
                == f"http://testserver/project/test/journal/view/{journal_page['id']}"
            )

    def test_comment(self):
        response = self.client.get("/rest/comment/")
        assert response.status_code == 200
        for comment in response.data:
            assert comment["absolute_url"] is None
