from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

data = {
    "file": "img.png",
    "type": "image",
}


class UserTestCase(APITestCase):
    def setUp(self):
        url = reverse("add-staff")
        cred = {
            "username": "user1",
            "email": "whatever@gmail.com",
            "password": "123456",
        }
        self.client.post(url, cred, format="json")

    def test_unauthenticated_request(self):
        url = reverse("s3-presigned")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 401)

    def test_authenticated_request(self):
        url = reverse("s3-presigned")
        cred = {
            "username": "user1",
            "password": "123456",
        }
        url = reverse("auth-token")
        response = self.client.post(url, cred, format="json")
        token = response.json()["token"]
        headers = {"Authorization": f"Token {token}"}
        response = self.client.post(url, cred, format="json", headers=headers)
        self.assertEqual(response.status_code, 200)
