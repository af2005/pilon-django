from django.contrib.auth import get_user_model, models
from django.test import TestCase

User = get_user_model()


class UsersManagersTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username="testuser", password="foo")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(ValueError):
            User.objects.create_user(username="")
        with self.assertRaises(ValueError):
            User.objects.create_user(username="", password="foo")

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(username="testadmin", password="foo")
        self.assertEqual(admin_user.username, "testadmin")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(username="testadmin", password="foo", is_superuser=False)

    def test_delete_user(self):
        user = User.objects.create_user(username="testuser", password="foo")
        user.delete()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username="testuser")
