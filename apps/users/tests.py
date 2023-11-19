from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class UserTestCase(APITestCase):
    def setUp(self):
        User.objects.create(
            username="admim",
            email="asgfsag@gmail.com",
            password="123456",
        )

    def test_users_required_to_have_an_email(self):
        """All users have emails"""
        user = User.objects.get(username="admim")
        self.assertNotEqual(user.email, None)

    def test_wrong_email_format(self):
        url = reverse("add-staff")
        data = {
            "username": "ummmmmm",
            "email": "rip",
            "password": "123456",
        }
        response = self.client.post(url, data, format="json")
        self.assertNotEqual(response.status_code, 201)
