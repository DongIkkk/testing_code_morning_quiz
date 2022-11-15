from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse


class UserSignUpTest(APITestCase):
    def test_signup(self):
        url = reverse("user_view")
        user_data = {
            "username":"testuser",
            "fullname":"testuser1",
            "email":"test@test.com",
            "password":"password",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.data["message"], "가입 완료!!")

