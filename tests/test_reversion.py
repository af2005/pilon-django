from django.test import TestCase

from www.models.entity import Entity
from www.models.user import User
import reversion
from reversion.models import Version


class TestReversion(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create_user(
            username="jacob", email="jacob@…", password="top_secret"
        )

    def test_revision_data(self):
        with reversion.create_revision():
            entity = Entity.objects.create(name="TestEntity", creator=self.user)
        with reversion.create_revision():
            entity.name = "TestEntityUpdated"
            entity.save()

        # Load a queryset of versions for a specific model instance.
        versions = Version.objects.get_for_object(entity)
        assert len(versions) == 2

        # Check the serialized data for the first version.
        assert versions[1].field_dict["name"] == "TestEntity"
        assert versions[0].field_dict["creator_id"] == self.user.id

        # Check the serialized data for the second version.
        assert versions[0].field_dict["name"] == "TestEntityUpdated"
        assert versions[0].field_dict["creator_id"] == self.user.id

    def test_revert_reversion(self):
        with reversion.create_revision():
            entity = Entity.objects.create(name="TestEntity", creator=self.user)

        with reversion.create_revision():
            entity.name = "TestEntityUpdated"
            entity.save()

        versions = Version.objects.get_for_object(entity)
        # Revert the first revision.
        versions[1].revision.revert()

        # Check the model instance has been reverted.
        entity.refresh_from_db()
        assert entity.name == "TestEntity"
        assert entity.creator == self.user

        # Revert the second revision.
        versions[0].revision.revert()

        # Check the model instance has been reverted.
        entity.refresh_from_db()
        assert entity.name == "TestEntityUpdated"
        assert entity.creator == self.user
