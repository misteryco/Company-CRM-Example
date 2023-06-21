from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, APITestCase

from rest_framework.response import Response
from rest_framework import status
from unittest.mock import patch
from crm_for_companies.api_employees.views import RegisterView


class RegisterViewTestCase(APITestCase):
    def test_register_view_success(self):
        # Create a mock request
        factory = APIRequestFactory()
        request = factory.post('/register/',
                               {'username': 'testuser', 'password': 'testpassword', 'email': 'test@example.com'})
        request.data = {'username': 'testuser', 'password': 'testpassword', 'email': 'test@example.com'}

        # Create a mock response
        mock_response = Response({"message": "Successfully registered.<Mock User>"}, status=status.HTTP_201_CREATED)

        with patch('crm_for_companies.api_employees.views.User.objects') as mock_user_objects:
            with patch('crm_for_companies.api_employees.views.send_welcome_email_to_new_users') as mock_send_email:
                # Configure the mock user object
                mock_user = User(username='testuser', email='test@example.com')
                mock_user.set_password('testpassword')
                mock_user.return_value = mock_user
                mock_user_objects.create.return_value = mock_user

                # Configure the mock email sending
                mock_send_email.delay.return_value = None

                # Instantiate the view and call the post method
                view = RegisterView()
                response = view.post(request)

                # Assertions
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                self.assertEqual(response.data, {"message": f"Successfully registered.<{mock_user}>"})

                # Verify the mock email sending
                # mock_user_objects.assert_called_once()
                mock_send_email.delay.assert_called_once()
