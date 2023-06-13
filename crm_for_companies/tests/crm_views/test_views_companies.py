from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase, Client
from django.urls import reverse

client = Client()


class TestCompany(APITestCase):
    def test_auth_user_name(self):
        sample_user = {
            "username": "SomeOneNew3",
            "password": "12345",
            "email": "some3@crazy.com",
            "first_name": "",
            "last_name": ""
        }
        # Here we send a request 'register_user' and response is saved in :
        # this a actual request/response cycle
        response = self.client.post(reverse('register_user'), sample_user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(reverse('api_token_auth'), {"username": "SomeOneNew3", "password": "12345"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = f"Token {response.data['token']}"

        self.client.credentials(HTTP_AUTHORIZATION=token)

        response = self.client.get(reverse('get user by token'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertJSONEqual(response.content.decode("utf-8"), {"userNameByToken": "SomeOneNew3"})
