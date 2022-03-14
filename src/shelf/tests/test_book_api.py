from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from ..models import Book


BOOK_CREATE_URL = reverse('book:create')
BOOK_LIST_URL = reverse('book:list')
BOOK_EDIT_URL = reverse('book:edit', args=[1])
payload = {
            'name': 'Капитал',
            'genre': 'политическая экономика',
            'page_number': 1000,
            'publisher': 'ACT',
            'author': 'Карл Маркс',
        }


class BookAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_book_create(self):
        response = self.client.post(BOOK_CREATE_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.first().name, payload.get('name'), msg='Название не совпадает')

    def test_book_edit(self):
        Book.objects.create(**payload)

        edit_data = {'name': 'Банковское дело', 'author': 'Максим Галкин'}
        response = self.client.patch(BOOK_EDIT_URL, edit_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.first().author, edit_data.get('author'), msg='Имя автора не совпадает')

    def test_book_delete(self):
        book = Book.objects.create(**payload)
        response = self.client.delete(BOOK_EDIT_URL)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertNotIn(book, Book.objects.all())
