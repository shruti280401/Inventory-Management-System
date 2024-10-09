# inventory/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Item

class ItemTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item_data = {'name': 'Test Item', 'description': 'A test item', 'quantity': 10}
        self.item = Item.objects.create(**self.item_data)

    def test_create_item(self):
        response = self.client.post(reverse('item-create'), self.item_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_item(self):
        response = self.client.get(reverse('item-detail', kwargs={'pk': self.item.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item.name)

    def test_update_item(self):
        new_data = {'name': 'Updated Item', 'description': 'Updated description', 'quantity': 5}
        response = self.client.put(reverse('item-detail', kwargs={'pk': self.item.pk}), new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item(self):
        response = self.client.delete(reverse('item-detail', kwargs={'pk': self.item.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# Create your tests here.
