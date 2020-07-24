import json
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from .models import UserProfile
from .serializers import UserProfileSerializer

User = get_user_model()
# Create your tests here.
class ProfileViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='test@mail.com', first_name='first', last_name='last', password='some-pw-entered')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token "+ str(self.token))

    def test_profile_list_authenticated(self):
        response = self.client.get("http://127.0.0.1:8080/api/profile/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
