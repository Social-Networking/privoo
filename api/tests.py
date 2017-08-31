from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from page.models import Post, MyUser


class PostTests(APITestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(email="test@test.pl", password="example")
        self.other_user = MyUser.objects.create_user(email="test2@test.pl", password="example2")

    def test_create_post(self):
        self.client.force_login(self.user)
        url = reverse('post-list')
        data = {'description': 'testowy'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.all()[0].owner, self.user)
